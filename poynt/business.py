from poynt import API


class Business():

    @classmethod
    def getBusiness(cls, business_id):
        """
        Gets a business by ID.
        """

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s' % business_id,
            method='GET'
        )
