"""
QUESTION:
Write a function `reverse_dict_order` that takes a dictionary with mixed type keys (numeric and string data types) and values as input, and returns a new dictionary with the keys in reverse order. The input dictionary has at least one string key, one integer key, one float key, and one tuple key. Empty strings or tuples are not valid inputs. The function should work with Python 3.7 and later.
"""

def reverse_dict_order(input_dict):
    """
    Returns a new dictionary with the keys in reverse order.

    Args:
        input_dict (dict): A dictionary with mixed type keys (numeric and string data types) and values.

    Returns:
        dict: A new dictionary with the keys in reverse order.
    """
    return {k: input_dict[k] for k in list(input_dict.keys())[::-1]}