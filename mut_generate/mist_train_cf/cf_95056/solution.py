"""
QUESTION:
Create a function named `merge_dicts` that takes two dictionaries, `dict1` and `dict2`, as input and returns a new dictionary that combines the key-value pairs from both dictionaries. If a key exists in both dictionaries, the value from `dict2` should overwrite the value from `dict1` unless the corresponding values are lists or dictionaries. If the values are lists, they should be concatenated. If the values are dictionaries, they should be merged recursively. If a key exists in only one dictionary, the key-value pair should be added to the combined dictionary.
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