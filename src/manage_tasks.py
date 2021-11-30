import argparse, sys
from pyral import Rally, rallyWorkset

options = [opt for opt in sys.argv[1:] if opt.startswith('--')]
server, user, password, apikey, workspace, project = rallyWorkset(options)
rally = Rally(server, user, password, workspace=workspace, project=project)



def get_tasks():
    columns = ["ID", "State", "Name", "Actuals"]
    formatting = "{:<15} {:<15} {:<35} {:>12}"
    story = rally.get('HierarchicalRequirement', fetch=True,
                  query='FormattedID = "US16436"', instance=True)
    
    # my_tasks = list of pyral Task objects
    my_tasks = list(filter(lambda x: x.Owner.EmailAddress == user, story.Tasks))

    print(formatting.format(*columns))
    [print(formatting.format(task.FormattedID, task.State, task.Name, task.Actuals)) for task in my_tasks]

def update_task():
    pass

def main():
    # if args.config, connect with rally-v2.0.cfg - MUST BE PRESENT
    # if args.get_tasks, run get_tasks() - requires US12345
    # if args.update_tasks, run update_task() - requires TA12345
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--get-tasks')
    parser.add_argument('--update-task')
    required = parser.add_argument_group('required arguments')
    required.add_argument('--config', help='Config file name', required=True)
    parser.parse_args()
    
    main()