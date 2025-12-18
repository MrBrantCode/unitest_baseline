"""
QUESTION:
Create a function `sort_dict_by_value` that sorts a dictionary by its values. The function should take a dictionary as input and return a list of tuples, where each tuple contains a key-value pair from the original dictionary, sorted in ascending order based on the dictionary values. The function should not modify the original dictionary.
"""

import operator

def sort_dict_by_value(dictionary):
    """
    Sorts a dictionary by its values in ascending order.

    Args:
        dictionary (dict): The input dictionary.

    Returns:
        list: A list of tuples containing key-value pairs from the original dictionary, sorted by value.
    """
    return sorted(dictionary.items(), key=operator.itemgetter(1))