"""
QUESTION:
Create a function called `common_keys` that takes a list of dictionaries as input and returns a new list of dictionaries. This new list should only contain dictionaries with keys that are present in all dictionaries of the input list and only include those common keys. If there are no common keys among the input dictionaries, the function should return an empty list.
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