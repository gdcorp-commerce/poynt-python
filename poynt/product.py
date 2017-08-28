from poynt import API
from poynt.helpers import json_patch


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
    def get_products_summary(cls, business_id, start_at=None, start_offset=None,
                             end_at=None, limit=None):
        """
        Get a list of product summaries at a business. Product summaries contain
        product shortCode, price, businessId, name, and id.

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
            url='/businesses/%s/products/summary' % business_id,
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

    @classmethod
    def create_product(cls, business_id, product):
        """
        Creates a product on a business.

        Arguments:
        business_id (str): the business ID
        product (dict): the full product object
        """

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/products' % business_id,
            method='POST',
            json=product,
        )

    @classmethod
    def delete_product(cls, business_id, product_id):
        """
        Deactivates a product. Deactivated products will be removed from all
        catalog references.

        Arguments:
        business_id (str): the business ID
        product_id (str): the product ID
        """

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/products/%s' % (business_id, product_id),
            method='DELETE'
        )

    @classmethod
    def update_product(cls, business_id, product_id, product=None, patch=None, no_remove=True):
        """
        Updates a product by ID. Can either specify the whole product, or an array
        of JSON Patch instructions.

        Arguments:
        business_id (str): the business ID
        product_id (str): the product ID

        Keyword arguments:
        product (dict): the full product object
        patch (list of dict): JSON Patch update instructions
        no_remove (boolean, optional): don't remove any keys from old product in the patch.
                                       safer this way. defaults to True
        """

        # get patch instructions if only product is specified
        if patch is None:
            if product is None:
                raise ValueError("Either patch or product must be specified")

            old_product, status_code = cls.get_product(business_id, product_id)
            if status_code >= 300 or old_product is None:
                raise RuntimeError("Product to patch not found")

            patch = json_patch(old_product, product, no_remove=no_remove)

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/products/%s' % (business_id, product_id),
            method='PATCH',
            json=patch,
        )
