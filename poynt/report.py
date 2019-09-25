from poynt import API


class Report():

    @classmethod
    def get_reports(cls, business_id, store_id=None, device_id=None, timezone=None, page=1, limit=25, report_type=None,
                    user_id=None, including_date=None):
        """
        Get reports at a business.

        Arguments:
        business_id (str): the business ID

        Keyword arguments:
        store_id (str, optional): the store ID
        device_id (str, optional): the device ID
        timezone (str, optional): the timezone
        page (int, optional): the page of reports to load. defaults to 1
        limit (int, optional): the number of reports to load per page. defaults to 25
        report_type (str, optional): report types to filter by
        user_id (str, optional): user id to filter by
        including_date (str, optional): show only reports whose time range overlaps to this date
        """

        params = {}
        if store_id is not None:
          params['storeId'] = store_id
        if device_id is not None:
          params['deviceId'] = device_id
        if timezone is not None:
          params['timezone'] = timezone
        if page is not None:
          params['page'] = page
        if limit is not None:
          params['limit'] = limit
        if report_type is not None:
          params['reportType'] = report_type
        if user_id is not None:
          params['userId'] = user_id
        if including_date is not None:
          params['includingDate'] = including_date

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/reports' % business_id,
            method='GET',
            params=params,
            app='WEB',
        )

    @classmethod
    def create_report(cls, business_id, report_type, start, end, store_id=None,
                      tid=None, employee_id=None, employee_name=None):
        """
        Creates a report at a business.

        Arguments:
        business_id (str): the business ID
        report_type (str): the report type
        start (str): ISO8601 formatted report start date/time
        end (str): ISO8601 formatted report end date/time

        Keyword arguments:
        store_id (str, optional): the store ID
        tid (str, optional): the tid
        employee_id (str, optional): the employee ID
        employee_name (str, optional): the employee name
        """

        params = {}
        params['type'] = report_type
        params['start'] = start
        params['end'] = end
        if store_id is not None:
          params['storeId'] = store_id
        if tid is not None:
          params['tid'] = tid
        if employee_id is not None:
          params['employeeId'] = employee_id
        if employee_name is not None:
          params['employeeName'] = employee_name

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/reports' % business_id,
            method='POST',
            json=params,
            app='WEB',
        )
