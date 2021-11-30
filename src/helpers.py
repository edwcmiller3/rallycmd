def get_rally_item(rally, item_type, query_str):
    return rally.get(item_type, fetch=True, query=query_str, instance=True)