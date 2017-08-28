from poynt import API


class Business():

    @classmethod
    def get_business(cls, business_id):
        """
        Gets a business by ID.

        Arguments:
        business_id (str): the business ID to get
        """

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s' % business_id,
            method='GET'
        )

    @classmethod
    def get_business_by_device_id(cls, device_id):
        """
        Get a business by a device id.

        Arguments:
        device_id (str): the device ID to get a business for
        """

        params = {
            'storeDeviceId': device_id
        }

        api = API.shared_instance()
        return api.request(
            url='/businesses',
            method='GET',
            params=params
        )
