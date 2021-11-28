# Proof of concept to check modules working and
# project setup correctly

import sys
from pyral import Rally, rallyWorkset

options = [opt for opt in sys.argv[1:] if opt.startswith('--')]
server, user, password, apikey, workspace, project = rallyWorkset(options)
rally = Rally(server, user, password, workspace=workspace, project=project)

# print(" ".join('|%s|' % opt for opt in [server, user, password, apikey, workspace, project]))

# query_criteria = 'FormattedID = "TC5535"'
# response = rally.get('TestCase', fetch=True, query=query_criteria)
# if response.errors:
#     sys.exit(1)
# for testCase in response:  # there should only be one qualifying TestCase
#     print(f"{testCase.Name}, {testCase.Type}, {testCase.LastVerdict}")

story = rally.get('HierarchicalRequirement', fetch=True, query='FormattedID = "US16436"', instance=True)
print(story.Name)
my_tasks = list(filter(lambda x: x.Owner.EmailAddress == user, story.Tasks))
columns = ["ID", "State", "Name", "Actuals (h)", "To Do (h)"]
# my_task_details = [my_tasks.FormattedID, my_tasks.State, my_tasks.Name, my_tasks.Actuals, my_tasks.ToDo]
a = [[task.FormattedID, task.State, task.Name, task.Actuals, task.ToDo] for task in my_tasks]
formatting = "{:<9} {:<10} {:<35} {:<12} {:<12}"
print(formatting.format(*columns))
print(formatting.format(*a))
# [print(task.FormattedID, task.State, task.Name, task.Actuals, task.ToDo) for task in my_tasks]