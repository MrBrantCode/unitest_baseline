"""
QUESTION:
Write a function `flatten_dict` that takes a dictionary as input and returns a flattened dictionary. The input dictionary may contain nested dictionaries of arbitrary depth. The keys of the output dictionary should be in the format "parentkey_childkey" for nested keys, where the parent key and child key are joined by an underscore. The input dictionary will only contain string keys and values of string, integer or boolean types.
"""

def flatten_dict(dictionary, parent_key='', sep='_'):
    flattened_dict = {}
    for key, value in dictionary.items():
        new_key = parent_key + sep + key if parent_key else key
        if isinstance(value, dict):
            flattened_dict.update(flatten_dict(value, new_key, sep))
        else:
            flattened_dict[new_key] = value
    return flattened_dict