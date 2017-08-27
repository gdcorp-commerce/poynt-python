from poynt import API


class Order():

    @classmethod
    def getOrders(cls, business_id, start_at=None, start_offset=None,
                  end_at=None, limit=None, card_number_first_6=None,
                  card_number_last_4=None, card_expiration_month=None,
                  card_expiration_year=None, card_holder_first_name=None,
                  card_holder_last_name=None, store_id=None):
        """
        Get all orders at a business by various criteria.

        Arguments:
        business_id -- the business ID

        Keyword arguments:
        start_at -- get orders created after this time in seconds
        start_offset -- the numeric offset to start the list (for pagination)
        end_at -- get orders created before this time in seconds
        limit -- how many orders to return (for pagination)
        card_number_first_6 -- return orders with card numbers starting with this
        card_number_last_4 -- return orders with card numbers ending with this
        card_expiration_month -- return orders with this card expiration month
        card_expiration_year -- return orders with this card expiration year
        card_holder_first_name -- return orders with first name matching this
        card_holder_last_name -- return orders with last name matching this
        store_id -- return orders from this store
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
        if store_id is not None:
            params['storeId'] = store_id

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/orders' % business_id,
            method='GET',
            params=params,
        )

    @classmethod
    def getOrder(cls, business_id, order_id):
        """
        Get a single order at a business.

        Arguments:
        business_id -- the business ID
        order_id -- the order ID
        """

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/orders/%s' % (business_id, order_id),
            method='GET'
        )
