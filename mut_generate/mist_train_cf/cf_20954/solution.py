"""
QUESTION:
Create a function `sort_dict_list` that sorts a list of dictionaries in ascending order of their "count" value while preserving the relative order of dictionaries with the same "count" value. Only include dictionaries that have a key "status" with the value "active".
"""

def sort_dict_list(data):
    active_dicts = [d for d in data if d.get('status') == 'active']
    sorted_dicts = sorted(active_dicts, key=lambda x: x['count'])
    return sorted_dicts