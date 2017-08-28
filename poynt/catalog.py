from poynt import API
from poynt.helpers import json_patch


class Catalog():

    @classmethod
    def get_catalogs(cls, business_id, start_at=None, start_offset=None,
                     end_at=None, limit=None):
        """
        Get all catalogs at a business.

        Arguments:
        business_id (str): the business ID

        Keyword arguments:
        start_at (int, optional): get catalogs created after this time in seconds
        start_offset (int, optional): the numeric offset to start the list (for pagination)
        end_at (int, optional): get catalogs created before this time in seconds
        limit (int, optional): how many catalogs to return (for pagination)
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
            url='/businesses/%s/catalogs' % business_id,
            method='GET',
            params=params,
        )

    @classmethod
    def get_catalog(cls, business_id, catalog_id):
        """
        Get a single catalog for a business.

        Arguments:
        business_id (str): the business ID
        catalog_id (str): the catalog ID
        """

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/catalogs/%s' % (business_id, catalog_id),
            method='GET'
        )

    @classmethod
    def get_full_catalog(cls, business_id, catalog_id):
        """
        Get a catalog by id with all product details info embedded in
        the Catalog.

        Arguments:
        business_id (str): the business ID
        catalog_id (str): the catalog ID
        """

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/catalogs/%s/full' % (business_id, catalog_id),
            method='GET'
        )

    @classmethod
    def create_catalog(cls, business_id, catalog):
        """
        Creates a catalog on a business.

        Arguments:
        business_id (str): the business ID
        catalog (dict): the catalog object
        """

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/catalogs' % business_id,
            method='POST',
            json=catalog,
        )

    @classmethod
    def create_full_catalog(cls, business_id, full_catalog):
        """
        Creates a catalog on a business with embedded products.
        This differs from create_catalog as you can create products
        and catalogs at the same time.

        Arguments:
        business_id (str): the business ID
        full_catalog (dict): the full catalog object
        """

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/catalogs/full' % business_id,
            method='POST',
            json=full_catalog,
        )

    @classmethod
    def update_catalog(cls, business_id, catalog_id, catalog=None, patch=None, no_remove=True):
        """
        Updates a catalog by ID. Can either specify the whole catalog, or an array
        of JSON Patch instructions.

        Arguments:
        business_id (str): the business ID
        catalog_id (str): the catalog ID

        Keyword arguments:
        catalog (dict): the catalog object. this should be a Catalog, not a CatalogWithProduct.
        patch (list of dict): JSON Patch update instructions
        no_remove (boolean, optional): don't remove any keys from old catalog in the patch.
                                       safer this way. defaults to True
        """

        # get patch instructions if only catalog is specified
        if patch is None:
            if catalog is None:
                raise ValueError("Either patch or catalog must be specified")

            old_catalog, status_code = cls.get_catalog(business_id, catalog_id)
            if status_code >= 300 or old_catalog is None:
                raise RuntimeError("Catalog to patch not found")

            patch = json_patch(old_catalog, catalog, no_remove=no_remove)

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/catalogs/%s' % (business_id, catalog_id),
            method='PATCH',
            json=patch,
        )

    @classmethod
    def delete_catalog(cls, business_id, catalog_id):
        """
        Deletes a single catalog for a business.

        Arguments:
        business_id (str): the business ID
        catalog_id (str): the catalog ID
        """

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/catalogs/%s' % (business_id, catalog_id),
            method='DELETE'
        )

    @classmethod
    def get_category(cls, business_id, catalog_id, category_id):
        """
        Get a single category in a catalog for a business.

        Arguments:
        business_id (str): the business ID
        catalog_id (str): the catalog ID
        category_id (str): the category ID
        """

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/catalogs/%s/categories/%s' % (
                business_id, catalog_id, category_id),
            method='GET'
        )

    @classmethod
    def create_category(cls, business_id, catalog_id, category):
        """
        Creates a category on a catalog on a business.

        Arguments:
        business_id (str): the business ID
        catalog_id (str): the catalog ID
        category (dict): the category object
        """

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/catalogs/%s/categories' % (
                business_id, catalog_id),
            method='POST',
            json=category,
        )

    @classmethod
    def lookup_categories(cls, business_id, catalog_id, category_ids):
        """
        Gets multiple categories on a catalog by IDs.

        Arguments:
        business_id (str): the business ID
        catalog_id (str): the catalog ID
        category_ids (list of str): a list of category ids
        """

        params = {
            'ids': category_ids
        }

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/catalogs/%s/categories/lookup' % (
                business_id, catalog_id),
            method='GET',
            params=params,
        )

    @classmethod
    def delete_category(cls, business_id, catalog_id, category_id):
        """
        Deletes a category by ID.

        Arguments:
        business_id (str): the business ID
        catalog_id (str): the catalog ID
        category_id (str): the category ID
        """

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/catalogs/%s/categories/%s' % (
                business_id, catalog_id, category_id),
            method='DELETE'
        )

    @classmethod
    def update_category(cls, business_id, catalog_id, category_id, category=None, patch=None, no_remove=True):
        """
        Updates a category by ID. Can either specify the whole category, or an array
        of JSON Patch instructions.

        Arguments:
        business_id (str): the business ID
        catalog_id (str): the catalog ID
        category_id (str): the category ID

        Keyword arguments:
        category (dict): the category object
        patch (list of dict): JSON Patch update instructions
        no_remove (boolean, optional): don't remove any keys from old category in the patch.
                                       safer this way. defaults to True
        """

        # get patch instructions if only category is specified
        if patch is None:
            if category is None:
                raise ValueError("Either patch or category must be specified")

            old_category, status_code = cls.get_category(
                business_id, catalog_id, category_id)
            if status_code >= 300 or old_category is None:
                raise RuntimeError("Category to patch not found")

            patch = json_patch(old_category, category, no_remove=no_remove)

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/catalogs/%s/categories/%s' % (
                business_id, catalog_id, category_id),
            method='PATCH',
            json=patch,
        )
