from poynt import API


class Store():

    @classmethod
    def get_store(cls, business_id, store_id):
        """
        Gets a store by ID.

        Arguments:
        business_id (str): the business ID
        store_id (str): the store ID
        """

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/stores/%s' % (business_id, store_id),
            method='GET'
        )
