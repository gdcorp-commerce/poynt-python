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
