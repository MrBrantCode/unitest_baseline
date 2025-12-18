"""
QUESTION:
Write a function `flatten_dict(nested_dict)` that takes a nested dictionary as input and returns a new dictionary with the nested keys concatenated with a dot (.) to represent the nesting. The function should recursively traverse the input dictionary and flatten it into a single-level dictionary.
"""

def entance(nested_dict, parent_key='', sep='.'):
    items = {}
    for key, value in nested_dict.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.update(entance(value, new_key, sep=sep))
        else:
            items[new_key] = value
    return items