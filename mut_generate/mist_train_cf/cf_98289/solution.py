"""
QUESTION:
Write a function `common_keys(dicts)` that takes a list of dictionaries `dicts` as input and returns a new list of dictionaries containing only the keys that appear in all dictionaries of the input list. The function should also handle cases where there are no common keys among the dictionaries by returning an empty list.
"""

def common_keys(dicts):
    if not dicts:
        return []
    keys = set(dicts[0].keys())
    for d in dicts[1:]:
        keys &= set(d.keys())
    if not keys:
        return []
    return [{k: d[k] for k in keys} for d in dicts if all(k in d for k in keys)]