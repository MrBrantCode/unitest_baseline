"""
QUESTION:
Access and modify a specific nested value in a dictionary. 

Create a function named `modify_nested_dict` that takes a dictionary, a list of nested keys, and a new value as parameters. The function should return the modified dictionary with the specified nested value updated. Assume that the nested keys exist in the dictionary.

Restrictions: The function should handle dictionaries with arbitrary levels of nesting.
"""

def modify_nested_dict(nested_dict, nested_keys, new_value):
    """
    Modify a specific nested value in a dictionary.

    Args:
    nested_dict (dict): The dictionary with nested values.
    nested_keys (list): A list of nested keys.
    new_value: The new value to be assigned.

    Returns:
    dict: The modified dictionary with the specified nested value updated.
    """
    current_dict = nested_dict
    for key in nested_keys[:-1]:
        current_dict = current_dict[key]
    current_dict[nested_keys[-1]] = new_value
    return nested_dict