"""
QUESTION:
Create a function `flatten_dict` that takes a dictionary `d` and a prefix string as input and returns a flattened dictionary. The function should recursively handle any level of nesting in the input dictionary, which may contain other dictionaries and lists. The function should update the keys of the flattened dictionary by appending the nested key names and indices.
"""

import pandas as pd

def flatten_dict(d, prefix=''):
    """
    Recursively flatten a dictionary and its nested values.

    Args:
        d (dict): The dictionary to be flattened.
        prefix (str): The prefix string for the keys in the flattened dictionary.

    Returns:
        dict: The flattened dictionary.
    """
    flattened = {}
    for key, value in d.items():
        if isinstance(value, dict):
            flattened.update(flatten_dict(value, prefix + key + '_'))
        elif isinstance(value, list):
            for i, item in enumerate(value):
                if isinstance(item, dict):
                    flattened.update(flatten_dict(item, prefix + key + '_' + str(i) + '_'))
                else:
                    flattened[prefix + key + '_' + str(i)] = item
        else:
            flattened[prefix + key] = value
    return flattened