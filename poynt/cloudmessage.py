from poynt import API


class CloudMessage():

    @classmethod
    def send_raw_cloud_message(cls, message):
        """
        Sends a cloud message by specifying the entire message object.

        Arguments:
        message (dict): the full cloud message object
        """

        api = API.shared_instance()
        return api.request(
            url='/cloudMessages',
            method='POST',
            json=message,
        )

    @classmethod
    def send_cloud_message(cls, business_id=None, store_id=None,
                           class_name=None, package_name=None, device_id=None,
                           serial_number=None, data='{}', collapse_key=None,
                           ttl=900):
        """
        Send a message from the cloud to your application running at a Poynt terminal.

        Keyword arguments:
        business_id (str): the business ID
        store_id (str): the store ID
        class_name (str): the class name of the receiver in your app
        package_name (str): the package name of your app
        device_id (str): the device ID
        serial_number (str): the serial number
        data (str, optional): the data to send. defaults to {}
        collapse_key (str, optional): dedupe messages on this key
        ttl (int, optional): how long until the cloud message expires. defaults
                             to 900 seconds
        """

        message = {
            'businessId': business_id,
            'storeId': store_id,
            'deviceId': device_id,
            'recipient': {
                'className': class_name,
                'packageName': package_name,
            },
        }

        if serial_number is not None:
            message['serialNum'] = serial_number
        if collapse_key is not None:
            message['collapseKey'] = collapse_key
        if ttl is not None:
            message['ttl'] = ttl
        if data is not None:
            message['data'] = data

        return cls.send_raw_cloud_message(message)
