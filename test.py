#!/usr/bin/env python

import poynt

poynt.application_id = 'urn:aid:7c4816cb-b025-4676-8b81-a4b2b821711d'
poynt.filename = '../poynt-node-test/keypair.pem'
poynt.env = 'dev'

# reports, status_code = poynt.Report.get_reports('8886bbd7-0fc1-47cf-ad36-21927e524ac1')

reports, status_code = poynt.Report.create_report('8886bbd7-0fc1-47cf-ad36-21927e524ac1', 'tips', start='2019-09-23', end='2019-09-24')

print status_code
print reports
