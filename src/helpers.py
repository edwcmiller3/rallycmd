import re

def get_rally_item(rally, item_type, query_str):
    item = parse_item(item_type)
    return rally.get(item, fetch=True, query=query_str, instance=True)

def fancy_display(heading, layout):
    pass

def parse_item(item):
    # Given arg from --list / --update determine the item type
    item_types = {
        'US': 'HierarchicalRequirement',
        'TA': 'Task',
        'DE': 'Defect',
        'TS': 'TestSet'
    }
    pattern = re.compile(r'(?P<prefix>[A-Z]+)\d+')
    result = pattern.findall(item)[0] if pattern.findall(item) else None
    return item_types[result] if result in item_types.keys() else None