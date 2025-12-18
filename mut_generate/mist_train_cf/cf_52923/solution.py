"""
QUESTION:
Create a function named `merge_dicts` that takes two dictionaries `dict1` and `dict2` as input and merges them into a single dictionary. The function should handle nested dictionaries by merging them recursively. If a key exists in both dictionaries and their values are dictionaries, the function should merge the nested dictionaries. If a key exists in both dictionaries and their values are not dictionaries, the function should use the value from `dict2`. If a key only exists in `dict2`, the function should add the key-value pair to the merged dictionary.
"""

def merge_dicts(dict1, dict2):
    for key in dict2:
        if key in dict1:
            if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                merge_dicts(dict1[key], dict2[key])
            else:
                dict1[key] = dict2[key]
        else:
            dict1[key] = dict2[key]
    return dict1