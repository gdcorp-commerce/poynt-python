import jwt
import requests
import time
import uuid

import poynt

poynt_urls = {
    'dev': 'https://services-dev.poynt.net',
    'ci': 'https://services-ci.poynt.net',
    'prod': 'https://services.poynt.net',
}

shared_instance = None


class API(object):

    def __init__(self, key=None, filename=None, env=None, application_id=None):
        """
        Instantiates the API class, which creates and authenticates requests
        to the Poynt API.

        Keyword arguments:
        key (str): the PEM-encoded private key associated with the application
        filename (str): the file where the PEM-encoded private key is stored
        env (str, optional): optional environment param. Defaults to "prod"
        application_id (str): your app's application ID
        """

        if key:
            self.key = key
        else:
            f = open(filename, 'r')
            self.key = f.read()

        self.application_id = application_id
        self.env = env

        self.api_version = '1.2'
        if env in poynt_urls:
            self.api_root = poynt_urls[env]
        else:
            self.api_root = poynt_urls['prod']

        self.session = requests.Session()
        self.access_token = None
        self.expires_at = None

    def request_headers(self):
        """
        Private method that generates request headers for Poynt API requests.
        """

        headers = {
            'User-Agent': 'python-sdk-%s' % self.application_id,
            'Api-Version': self.api_version,
            'Poynt-Request-Id': str(uuid.uuid4()),
        }

        if self.access_token:
            headers['Authorization'] = 'Bearer %s' % self.access_token

        return headers

    def naked_request(self, method, url, json=None, headers=None, form=None,
                      params=None):
        """
        Private method that makes a request to Poynt APIs without error protection.
        You shouldn't use this in your SDK methods.

        Arguments:
        method (str): the request method, e.g. GET, POST, PATCH, etc.
        url (str): the request relative URL, e.g. /businesses

        Keyword arguments:
        json (dict, optional): request data to send, encoded as JSON
        headers (dict, optional): request headers to send
        form (dict, optional): request data to send, encoded as a form. Use this or json
        params (dict, optional): request params to send in the querystring
        """

        headers = self.request_headers()
        method = method or 'GET'

        if form:
            r = self.session.request(
                method,
                url=self.api_root + url,
                data=form,
                headers=headers,
                params=params,
            )
        else:
            r = self.session.request(
                method,
                url=self.api_root + url,
                json=json,
                headers=headers,
                params=params,
            )

        return r.json(), r.status_code

    def access_token_is_expired(self):
        """
        Private method that tells you if your access token doesn't exist,
        or is expired.
        """

        if self.access_token is None:
            return True

        my_jwt = jwt.decode(self.access_token, verify=False)

        if my_jwt['exp'] < int(round(time.time())) + 60:
            return True

        return False

    def authenticate(self):
        """
        Authenticates with Poynt API using your application private key.
        """

        now = int(round(time.time() * 1000))
        my_jwt = jwt.encode({
            'aud': self.api_root,
            'iss': self.application_id,
            'sub': self.application_id,
            'iat': now,
            'jti': str(uuid.uuid4()),
            'exp': now + 1000 * 60 * 60 * 24 * 365,
        }, self.key, algorithm='RS256')

        json, status_code = self.naked_request(
            method='POST',
            url='/token',
            form={
                'grantType': 'urn:ietf:params:oauth:grant-type:jwt-bearer',
                'assertion': my_jwt
            }
        )

        if json is not None:
            self.access_token = json['accessToken']
            self.expires_at = now + json['expiresIn']

    def request(self, method, url, json=None, headers=None, form=None,
                params=None, force_token_refresh=False):
        """
        Makes a request against API service. Refreshes your access token if
        necessary. Use this for all requests in the SDK!

        Arguments:
        method (str): the request method, e.g. GET, POST, PATCH, etc.
        url (str): the request relative URL, e.g. /businesses

        Keyword arguments:
        json (dict, optional): request data to send, encoded as JSON
        headers (dict, optional): request headers to send
        form (dict, optional): request data to send, encoded as a form. Use this or JSON
        params (dict, optional): request params to send in the querystring
        force_token_refresh (bool, optional): whether to force refresh the access token or not
        """

        if self.access_token_is_expired() or force_token_refresh:
            self.authenticate()

        json, status_code = self.naked_request(
            method=method,
            url=url,
            json=json,
            headers=headers,
            form=form,
            params=params,
        )

        if status_code is 401 and json['code'] is 'INVALID_ACCESS_TOKEN':
            return self.request(
                method=method,
                url=url,
                json=json,
                headers=headers,
                form=form,
                params=params,
                force_token_refresh=True,
            )

        return json, status_code

    @classmethod
    def shared_instance(cls):
        """
        Gets a shared instance of API for making requests, so we can use the
        same access token globally in our application.
        """

        global shared_instance

        if shared_instance is not None:
            return shared_instance

        shared_instance = cls(
            key=poynt.key,
            filename=poynt.filename,
            env=poynt.env,
            application_id=poynt.application_id
        )

        return shared_instance
