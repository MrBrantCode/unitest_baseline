"""
QUESTION:
Write a function `remove_keys_from_dict(d, keys)` that takes a dictionary `d` and a list of keys `keys` as input. The function should return a new dictionary with all keys in `keys` removed from `d`, including nested dictionaries. If a value in `d` is a list, the function should also recursively remove keys from any dictionaries found within the list. Note that the function should not modify the original dictionary.
"""

def remove_keys_from_dict(d, keys):
    if isinstance(d, dict):
        return {k: remove_keys_from_dict(v, keys) for k, v in d.items() if k not in keys}
    elif isinstance(d, list):
        return [remove_keys_from_dict(x, keys) for x in d]
    else:
        return d