"""
QUESTION:
Write a function named `common_keys` that takes a list of dictionaries as input. The function should return a new list of dictionaries containing only the keys that appear in all dictionaries of the input list. If there are no common keys among the dictionaries, the function should return an empty list.
"""

def entrance(dicts):
    if not dicts:
        return []
    keys = set(dicts[0].keys())
    for d in dicts[1:]:
        keys &= set(d.keys())
    if not keys:
        return []
    return [{k: d[k] for k in keys} for d in dicts if all(k in d for k in keys)]