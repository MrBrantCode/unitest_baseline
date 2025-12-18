"""
QUESTION:
Write a function called `clone_list` that clones a list along with its nested elements. The input list may contain multiple data types including integers, strings, floats, and nested lists. The function should return a deep copy of the input list.
"""

import copy

def clone_list(input_list):
    """
    Creates a deep copy of the input list along with its nested elements.

    Args:
        input_list (list): The input list to be cloned.

    Returns:
        list: A deep copy of the input list.
    """
    return copy.deepcopy(input_list)