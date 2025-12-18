"""
QUESTION:
Create a function `sort_list_of_dicts` that takes a list of dictionaries and three keys (`key1`, `key2`, `key3`) as arguments. The function should return the sorted list of dictionaries. The sorting criteria should be as follows: 
- `key1` in ascending order (case-insensitive), 
- then `key2` in ascending order, 
- and finally `key3` in descending order.
"""

def sort_list_of_dicts(lst, key1, key2, key3):
    sorted_list = sorted(lst, key=lambda x: (x[key1].lower(), x[key2], -x[key3]))
    return sorted_list