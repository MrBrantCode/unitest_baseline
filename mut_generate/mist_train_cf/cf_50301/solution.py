"""
QUESTION:
Create a function `create_custom_dict` that takes two lists of equal length as input, `keys_list` and `values_list`, and returns a dictionary where the elements of `keys_list` are the keys and the elements of `values_list` are the values. The function should also filter the resulting dictionary to only include items with a value greater than or equal to 20.
"""

def create_custom_dict(keys_list, values_list):
    """
    Create a dictionary from two lists with a filter criteria.

    Args:
    keys_list (list): List of keys for the dictionary.
    values_list (list): List of values for the dictionary.

    Returns:
    dict: A dictionary where the elements of keys_list are the keys and the elements of values_list are the values,
          filtered to only include items with a value greater than or equal to 20.
    """
    return {key: value for key, value in zip(keys_list, values_list) if value >= 20}