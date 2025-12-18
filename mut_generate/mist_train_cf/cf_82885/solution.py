"""
QUESTION:
Write a function named `sort_dict` that accepts a dictionary and a flag as parameters and returns the dictionary sorted by values and then by keys. The flag parameter is optional and defaults to `True`, indicating ascending order. If the flag is `False`, the dictionary should be sorted in descending order.
"""

def sort_dict(dict_map, ascending=True):
    items = list(dict_map.items())
    sorted_items = sorted(items, key=lambda x: (x[1], x[0]), reverse=not ascending)
    sorted_dict = dict(sorted_items)
    return sorted_dict