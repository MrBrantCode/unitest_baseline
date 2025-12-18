"""
QUESTION:
Create a function `flatten_dict` that retrieves all the values from a nested dictionary and returns them in a flattened list. The function should be able to handle dictionaries with multiple levels of nesting. The input dictionary is not guaranteed to have a specific structure, and the function should work with any valid dictionary. The function should return a list of strings.
"""

def flatten_dict(dictionary):
    """Retrieves all the values from a nested dictionary and returns them in a flattened list."""
    flattened_list = []
    for value in dictionary.values():
        if isinstance(value, dict):
            flattened_list.extend(flatten_dict(value))
        else:
            flattened_list.append(value)
    return flattened_list