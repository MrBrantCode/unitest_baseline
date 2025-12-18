"""
QUESTION:
Implement a function `search_dict(d, keys)` that searches a dictionary `d` created from a valid JSON string using a given multi-level key string `keys` in the format "level1.level2.level3". The function should return the value associated with the key if found, otherwise return None. The dictionary may contain nested objects and arrays.
"""

import json

def search_dict(d, keys):
    if "." in keys:
        key, rest = keys.split(".", 1)
        return search_dict(d.get(key, {}), rest)
    else:
        return d.get(keys)