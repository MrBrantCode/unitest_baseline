"""
QUESTION:
Implement a function `copy_list` that takes a list as input and returns two lists: a shallow copy and a deep copy of the input list. The function should use the `copy` module in Python to create the shallow and deep copies. The input list may contain primitive and non-primitive sub-objects like lists or dictionaries.
"""

import copy

def copy_list(input_list):
    """
    Returns a shallow copy and a deep copy of the input list.

    Args:
        input_list (list): The list to be copied.

    Returns:
        tuple: A tuple containing the shallow copy and the deep copy of the input list.
    """
    shallow_copy = copy.copy(input_list)
    deep_copy = copy.deepcopy(input_list)
    return shallow_copy, deep_copy