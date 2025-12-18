"""
QUESTION:
Write a function `remove_duplicates` that takes a list of elements as input and returns a new list with duplicates removed while maintaining the original order of elements.
"""

from collections import OrderedDict

def remove_duplicates(input_list):
    """
    This function takes a list of elements as input and returns a new list with duplicates removed while maintaining the original order of elements.

    Args:
        input_list (list): A list of elements.

    Returns:
        list: A new list with duplicates removed.
    """
    return list(OrderedDict.fromkeys(input_list))