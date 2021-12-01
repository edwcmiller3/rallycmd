import argparse
import helpers
from pyral import Rally, rallyWorkset


def get_my_tasks(rally, id):
    columns = ["ID", "State", "Name", "Actuals"]
    query_str = f'FormattedID = "{id}"'
    formatting = "{:<12} {:<13} {:<35} {:>12}"

    story_obj = helpers.get_rally_item(
        rally, id, query_str)

    # my_tasks = list of pyral Task objects
    my_tasks = list(
        filter(lambda x: x.Owner.EmailAddress == rally.user, story_obj.Tasks))

    # TODO: Make this better
    # print(story.Name)
    print(formatting.format(*columns))
    [print(formatting.format(task.FormattedID, task.State,
           task.Name, task.Actuals)) for task in my_tasks]


def update_task():
    pass


def main(args):
    # if args.get_tasks, run get_tasks() - requires US12345
    # if args.update_tasks, run update_task() - requires TA12345
    # Handle empty string after password in .cfg for some reason
    server, user, password, workspace, project = filter(
        lambda x: x != '', rallyWorkset(args.config))
    rally = Rally(server, user, password, workspace=workspace, project=project)

    if args.list:
        get_my_tasks(rally, args.list)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--list')
    parser.add_argument('--update')
    required = parser.add_argument_group('required arguments')
    required.add_argument('--config', help='Config file name', required=True)
    args = parser.parse_args()

    main(args)
