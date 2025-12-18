"""
QUESTION:
Create a function named `flatten_dict` that takes a dictionary as input and returns a new dictionary where any nested dictionaries are flattened into a single level. The function should handle nested dictionaries of arbitrary depth, and the keys of the output dictionary should be in the format "parentkey_childkey" for nested keys, using an underscore as the separator. The input dictionary is guaranteed to only contain string keys and values of string, integer, or boolean types.
"""

def flatten_dict(nested_dict, parent_key='', sep='_'):
    flattened_dict = {}
    for key, value in nested_dict.items():
        new_key = parent_key + sep + key if parent_key else key
        if isinstance(value, dict):
            flattened_dict.update(flatten_dict(value, new_key, sep))
        else:
            flattened_dict[new_key] = value
    return flattened_dict