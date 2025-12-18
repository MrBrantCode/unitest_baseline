"""
QUESTION:
Create a function `merge_dicts` that takes two dictionaries, `dict1` and `dict2`, as input and returns a new dictionary, `combined_dict`. The function should merge the key-value pairs from both dictionaries into `combined_dict`. If a key exists in both dictionaries, the value from `dict2` should overwrite the value from `dict1`, except when the values are lists or dictionaries, in which case they should be concatenated or merged recursively, respectively. The function should handle cases where one or both dictionaries are empty.
"""

def merge_dicts(dict1, dict2):
    combined_dict = {}

    for key, value in dict1.items():
        if key in dict2:
            if isinstance(value, list) and isinstance(dict2[key], list):
                combined_dict[key] = value + dict2[key]
            elif isinstance(value, dict) and isinstance(dict2[key], dict):
                combined_dict[key] = merge_dicts(value, dict2[key])
            else:
                combined_dict[key] = dict2[key]
        else:
            combined_dict[key] = value

    for key, value in dict2.items():
        if key not in dict1:
            combined_dict[key] = value

    return combined_dict