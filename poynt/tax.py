from poynt import API


class Tax():

    @classmethod
    def get_taxes(cls, business_id, start_at=None, start_offset=None,
                  end_at=None, limit=None):
        """
        Get a list of taxes at a business.

        Arguments:
        business_id (str): the business ID

        Keyword arguments:
        start_at (int, optional): get taxes created after this time in seconds
        start_offset (int, optional): the numeric offset to start the list (for pagination)
        end_at (int, optional): get taxes created before this time in seconds
        limit (int, optional): how many taxes to return (for pagination)
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

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/taxes' % business_id,
            method='GET',
            params=params,
        )

    @classmethod
    def get_tax(cls, business_id, tax_id):
        """
        Get a single tax for a business.

        Arguments:
        business_id (str): the business ID
        tax_id (str): the tax ID
        """

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/taxes/%s' % (business_id, tax_id),
            method='GET'
        )
