# Proof of concept to check modules working and
# project setup correctly

import sys
from pyral import Rally, rallyWorkset

options = [opt for opt in sys.argv[1:] if opt.startswith('--')]
server, user, password, apikey, workspace, project = rallyWorkset(options)
rally = Rally(server, user, password, workspace=workspace, project=project)

# print(" ".join('|%s|' % opt for opt in [server, user, password, apikey, workspace, project]))

query_criteria = 'FormattedID = "TC5535"'
response = rally.get('TestCase', fetch=True, query=query_criteria)
if response.errors:
    sys.exit(1)
for testCase in response:  # there should only be one qualifying TestCase
    print(f"{testCase.Name}, {testCase.Type}, {testCase.LastVerdict}")