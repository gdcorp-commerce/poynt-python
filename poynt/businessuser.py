from poynt import API


class BusinessUser():

    @classmethod
    def getBusinessUsers(cls, business_id):
        """
        Get all users at a business.

        Arguments:
        business_id -- the business ID
        """

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/businessUsers' % business_id,
            method='GET'
        )

    @classmethod
    def getBusinessUser(cls, business_id, business_user_id):
        """
        Get a single user at a business.

        Arguments:
        business_id -- the business ID
        business_user_id -- the user ID
        """

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/businessUsers/%s' % (
                business_id, business_user_id),
            method='GET'
        )
