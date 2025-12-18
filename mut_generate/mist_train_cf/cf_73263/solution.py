"""
QUESTION:
Write a function `deepmerge(dict1, dict2)` that merges two deeply nested dictionaries `dict1` and `dict2` into one. If a key exists in both dictionaries, and both values are dictionaries, merge them recursively. If a key exists in both dictionaries but one or both values are not dictionaries, combine the values into a list in the order they appear in the original dictionaries.
"""

import json

def deepmerge(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            if isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = deepmerge(result[key], value)
            else:
                if not isinstance(result[key], list):
                    result[key] = [result[key]]
                result[key].append(value)
        else:
            result[key] = value
    return result