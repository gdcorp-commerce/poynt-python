from poynt import API


class Product():

    @classmethod
    def get_products(cls, business_id, start_at=None, start_offset=None,
                     end_at=None, limit=None):
        """
        Get a list of products at a business.

        Arguments:
        business_id (str): the business ID

        Keyword arguments:
        start_at (int, optional): get products created after this time in seconds
        start_offset (int, optional): the numeric offset to start the list (for pagination)
        end_at (int, optional): get products created before this time in seconds
        limit (int, optional): how many products to return (for pagination)
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
            url='/businesses/%s/products' % business_id,
            method='GET',
            params=params,
        )

    @classmethod
    def lookup_products(cls, business_id, product_ids):
        """
        Get a list of products by ID.

        Arguments:
        business_id (str): the business ID
        product_ids (list of str): a list of product ids
        """

        params = {
            'ids': product_ids
        }

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/products/lookup' % business_id,
            method='GET',
            params=params,
        )

    @classmethod
    def get_product(cls, business_id, product_id):
        """
        Get a single product for a business.

        Arguments:
        business_id (str): the business ID
        product_id (str): the product ID
        """

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/products/%s' % (business_id, product_id),
            method='GET'
        )
