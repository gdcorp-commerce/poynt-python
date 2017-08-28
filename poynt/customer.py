from poynt import API


class Customer():

    @classmethod
    def get_customers(cls, business_id, start_at=None, start_offset=None,
                      end_at=None, limit=None, card_number_first_6=None,
                      card_number_last_4=None, card_expiration_month=None,
                      card_expiration_year=None, card_holder_first_name=None,
                      card_holder_last_name=None):
        """
        Get all customers of a business by various criteria.

        Arguments:
        business_id (str): the business ID

        Keyword arguments:
        start_at (int, optional): get customers created after this time in seconds
        start_offset (int, optional): the numeric offset to start the list (for pagination)
        end_at (int, optional): get customers created before this time in seconds
        limit (int, optional): how many customers to return (for pagination)
        card_number_first_6 (str, optional): return customers with card numbers starting with this
        card_number_last_4 (str, optional): return customers with card numbers ending with this
        card_expiration_month (str, optional): return customers with this card expiration month
        card_expiration_year (str, optional): return customers with this card expiration year
        card_holder_first_name (str, optional): return customers with first name matching this
        card_holder_last_name (str, optional): return customers with last name matching this
        """

        params = {}
        if start_at is not None:
            params['startAt'] = start_at
        if start_offset is not None:
            params['startOffset'] = start_offset
        if end_at is not None:
            params['endAt'] = end_at
        if limit is not None:
            params['limit'] = limit
        if card_number_first_6 is not None:
            params['cardNumberFirst6'] = card_number_first_6
        if card_number_last_4 is not None:
            params['cardNumberLast4'] = card_number_last_4
        if card_expiration_month is not None:
            params['cardExpirationMonth'] = card_expiration_month
        if card_expiration_year is not None:
            params['cardExpirationYear'] = card_expiration_year
        if card_holder_first_name is not None:
            params['cardHolderFirstName'] = card_holder_first_name
        if card_holder_last_name is not None:
            params['cardHolderLastName'] = card_holder_last_name

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/customers' % business_id,
            method='GET',
            params=params,
        )

    @classmethod
    def get_customer(cls, business_id, customer_id):
        """
        Get a single customer at a business.

        Arguments:
        business_id (str): the business ID
        customer_id (str): the customer ID
        """

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/customers/%s' % (business_id, customer_id),
            method='GET'
        )
