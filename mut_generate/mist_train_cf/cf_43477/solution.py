"""
QUESTION:
Write a function `merge_dicts(dict1, dict2)` that recursively merges two nested dictionaries `dict1` and `dict2`. In case of conflicting key-value pairs, the value from `dict2` should be taken. The function should handle edge cases where a dictionary may be nested within itself. The input dictionaries may have non-dictionary values, and the function should not throw a TypeError in such cases.
"""

def merge_dicts(dict1, dict2):
    for k in dict2:
        if k in dict1 and isinstance(dict1[k], dict) and isinstance(dict2[k], dict):
            merge_dicts(dict1[k], dict2[k])
        else:
            dict1[k] = dict2[k]
    return dict1