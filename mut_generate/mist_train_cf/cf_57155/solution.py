"""
QUESTION:
Write a function named `reverse_dict_keys` that takes a dictionary as an argument and returns a new dictionary with the same keys and values as the original dictionary, but with the keys in reverse order. Assume that the input dictionary is an ordered dictionary (Python 3.7 or higher). The function should not sort the dictionary by values, only reverse the order of the keys.
"""

def reverse_dict_keys(input_dict):
    """
    Reverses the order of keys in a dictionary.

    Args:
    input_dict (dict): The input dictionary.

    Returns:
    dict: A new dictionary with the same keys and values as the original dictionary, 
          but with the keys in reverse order.
    """
    keys = list(input_dict.keys())
    keys.reverse()
    return {key: input_dict[key] for key in keys}