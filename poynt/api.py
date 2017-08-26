import cryptography
import uuid
import requests

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
        to the Poynt API
        """

        if key:
            self.key = key
        else:
            file = open(filename, 'r')
            self.key = file.read()

        self.application_id = application_id
        self.env = env

        self.api_version = '1.2'
        if env in poynt_urls:
            self.api_root = poynt_urls[env]
        else:
            self.api_root = poynt_urls['prod']

        self.session = requests.Session()
        self.access_token = None

    def request_headers(self):
        """
        Generates request headers for Poynt API requests
        """

        headers = {
            'User-Agent': 'python-sdk-%s' % self.application_id,
            'Api-Version': self.api_version,
            'Poynt-Request-Id': str(uuid.uuid4()),
            'Authorization': 'Bearer %s' % self.access_token,
        }

        return headers

    def naked_request(self, method, url, data=None, headers=None):
        """
        Makes a request to Poynt APIs without error protection
        """

        headers = self.request_headers()
        method = method or 'GET'

        r = self.session.request(
            method,
            url=self.api_root + url,
            data=data,
            headers=headers,
        )

        return r.json()

    @classmethod
    def shared_instance(cls):
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
