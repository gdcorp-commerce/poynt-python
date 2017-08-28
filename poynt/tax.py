from poynt import API
from poynt.helpers import json_patch


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

    @classmethod
    def create_tax(cls, business_id, tax):
        """
        Creates a tax on a business.

        Arguments:
        business_id (str): the business ID
        tax (dict): the full tax object
        """

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/taxes' % business_id,
            method='POST',
            json=tax,
        )

    @classmethod
    def delete_tax(cls, business_id, tax_id):
        """
        Deletes a tax.

        Arguments:
        business_id (str): the business ID
        tax_id (str): the tax ID
        """

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/taxes/%s' % (business_id, tax_id),
            method='DELETE'
        )

    @classmethod
    def update_tax(cls, business_id, tax_id, tax=None, patch=None, no_remove=True):
        """
        Updates a tax by ID. Can either specify the whole tax, or an array
        of JSON Patch instructions.

        Arguments:
        business_id (str): the business ID
        tax_id (str): the tax ID

        Keyword arguments:
        tax (dict): the full tax object
        patch (list of dict): JSON Patch update instructions
        no_remove (boolean, optional): don't remove any keys from old tax in the patch.
                                       safer this way. defaults to True
        """

        # get patch instructions if only tax is specified
        if patch is None:
            if tax is None:
                raise ValueError("Either patch or tax must be specified")

            old_tax, status_code = cls.get_tax(business_id, tax_id)
            if status_code >= 300 or old_tax is None:
                raise RuntimeError("Tax to patch not found")

            patch = json_patch(old_tax, tax, no_remove=no_remove)

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/taxes/%s' % (business_id, tax_id),
            method='PATCH',
            json=patch,
        )
