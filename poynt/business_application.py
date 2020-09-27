from poynt import API

class BusinessApplication():
    """
    A Class providing methods to fetch business application information

    """

    @classmethod
    def get_business_application(cls, business_id):
        """
        Gets a business application

        Arguments:
        business_id (str): the business ID of the business
        """
        api = API.shared_instance()
        return api.request(
            url='/businesses/' + business_id + '/payfac-application',
            method='GET',
            app='WEB',
        )

    @classmethod
    def get_business_account(cls, business_id):
        """
        Get account information related to the business

        Arguments:
        business_id (str): the business ID of the business
        """

        api = API.shared_instance()
        return api.request(
            url='/businesses/' + business_id + '/payfac-application/account',
            method='GET',
            app='WEB',
        )

    @classmethod
    def get_business_orders(cls, business_id):
        """
        Gets the orders attached to business application

        Arguments:
        business_id (str): the business ID of the business
        """

        api = API.shared_instance()
        return api.request(
            url='/businesses/' + business_id +
                '/payfac-application/orders',
            method='GET',
            app='WEB',
        )

    @classmethod
    def get_business_application_status(cls, business_id):
        """
        Get the status of business application

        Arguments:
        business_id (str): the business ID of the business
        """

        api = API.shared_instance()
        return api.request(
            url='/businesses/' + business_id +
                '/payfac-application/status',
            method='GET',
            app='WEB',
        )

    @classmethod
    def get_business_application_profile(cls, business_id):
        """
        Get business profile info

        Arguments:
        business_id (str): the business ID of the business
        """

        api = API.shared_instance()
        return api.request(
            url='/businesses/' + business_id +
                '/payfac-application/profile',
            method='GET',
            app='WEB',
        )
