from poynt import API


class Hook():

    @classmethod
    def getHooks(cls, business_id):
        """
        Gets a list of hooks currently subscribed to.

        Arguments:
        business_id -- use a merchant business ID to see what webhooks your app
                       is subscribed to for that merchant. use your own organization
                       ID to see your app billing webhooks, etc.
        """

        params = {
            'businessId': business_id
        }

        api = API.shared_instance()
        return api.request(
            url='/hooks',
            method='GET',
            params=params,
        )

    @classmethod
    def createHook(cls, business_id, delivery_url, secret=None, event_type=None,
                   event_types=None):
        """
        Subscribes to a webhook.

        Arguments:
        business_id -- the business ID to subscribe to a hook for. Use a merchant
                       business ID to subscribe to their e.g. transaction hooks;
                       use your own organization ID to subscribe to app billing, etc.
        delivery_url -- the URL to deliver webhooks to.

        Keyword arguments:
        secret -- used to sign the webhook event, so you can verify.
        event_type -- a single event type to subscribe to webhooks for.
        event_types -- a list of event types to subscribe to webhooks for.
        """

        api = API.shared_instance()

        json = {
            'applicationId': api.application_id,
            'businessId': business_id,
            'deliveryUrl': delivery_url,
        }
        if secret is not None:
            json['secret'] = secret
        if event_types is not None:
            json['eventTypes'] = event_types
        elif event_type is not None:
            json['eventTypes'] = [event_type]

        return api.request(
            url='/hooks',
            method='POST',
            json=json,
        )
