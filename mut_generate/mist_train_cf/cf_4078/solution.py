"""
QUESTION:
Create a function called `flatten_dict` that takes a nested dictionary as input and returns a list of its values in descending order. The function should work with dictionaries of any depth, not just a fixed number of levels.
"""

def flatten_dict(nested_dict):
    """
    This function takes a nested dictionary as input and returns a list of its values in descending order.

    Args:
    nested_dict (dict): The dictionary to be flattened.

    Returns:
    list: A list of dictionary values in descending order.
    """
    values = []
    for value in nested_dict.values():
        if isinstance(value, dict):
            values.extend(flatten_dict(value))
        else:
            values.append(value)
    return sorted(values, reverse=True)