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

# Get task names for story
owner_name = "Eddie" # DISPLAY NAME
# target_owner = rally.getUserInfo(username='edward.miller@acatoim.com') 
# OR 
# target_owner = rally.getUserInfo(name=owner_name)


story = rally.get('HierarchicalRequirement', fetch=True, query='FormattedID = "US16436"', instance=True)
for task in story.Tasks:
    if task.Owner.DisplayName == owner_name:
        print(task.FormattedID, task.Name, task.State)