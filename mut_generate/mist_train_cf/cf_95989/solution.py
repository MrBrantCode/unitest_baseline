"""
QUESTION:
Create a function `copy_list` that takes a nested list as an argument and returns a new list with the same structure and elements as the original list, but with the ability to modify nested lists without affecting the original list.
"""

import copy

def copy_list(nested_list):
    """
    Creates a new list with the same structure and elements as the original list,
    with the ability to modify nested lists without affecting the original list.

    Args:
        nested_list (list): The original nested list.

    Returns:
        list: A deep copy of the original list.
    """
    return copy.deepcopy(nested_list)