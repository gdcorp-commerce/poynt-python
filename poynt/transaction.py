from poynt import API


class Transaction():

    @classmethod
    def getTransactions(cls, business_id, start_at=None, start_offset=None,
                        end_at=None, limit=None, card_number_first_6=None,
                        card_number_last_4=None, card_expiration_month=None,
                        card_expiration_year=None, card_holder_first_name=None,
                        card_holder_last_name=None, store_id=None, device_id=None,
                        search_key=None, action=None, status=None, transaction_ids=None,
                        auth_only=None, unsettled_only=None, credit_debit_only=None):
        """
        Get all transactions at a business by various criteria.

        Arguments:
        business_id -- the business ID

        Keyword arguments:
        start_at -- get txns created after this time in seconds
        start_offset -- the numeric offset to start the list (for pagination)
        end_at -- get txns created before this time in seconds
        limit -- how many txns to return (for pagination)
        card_number_first_6 -- return txns with card numbers starting with this
        card_number_last_4 -- return txns with card numbers ending with this
        card_expiration_month -- return txns with this card expiration month
        card_expiration_year -- return txns with this card expiration year
        card_holder_first_name -- return txns with first name matching this
        card_holder_last_name -- return txns with last name matching this
        store_id -- return txns from this store
        device_id -- return txns from this device
        search_key -- instead of specifying which exact field to look at, the
                      client can simply pass this search key and the server will
                      look at various different fields,
        action -- only fetch txns with this action
        status -- only fetch txns with this status
        transaction_ids -- only fetch txns matching these ids (comma separated)
        auth_only - only fetch auth only txns
        unsettled_only - only fetch unsettled txns
        credit_debit_only - only fetch credit/debit txns
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
        if device_id is not None:
            params['deviceId'] = device_id
        if search_key is not None:
            params['searchKey'] = search_key
        if action is not None:
            params['action'] = action
        if status is not None:
            params['status'] = status
        if transaction_ids is not None:
            params['transactionIds'] = transaction_ids
        if auth_only is not None:
            params['authOnly'] = auth_only
        if unsettled_only is not None:
            params['unsettledOnly'] = unsettled_only
        if credit_debit_only is not None:
            params['creditDebitOnly'] = credit_debit_only

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/transactions' % business_id,
            method='GET',
            params=params,
        )

    @classmethod
    def getTransaction(cls, business_id, transaction_id):
        """
        Get a single transaction at a business.

        Arguments:
        business_id -- the business ID
        transaction_id -- the transaction ID
        """

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/transactions/%s' % (
                business_id, transaction_id),
            method='GET'
        )
