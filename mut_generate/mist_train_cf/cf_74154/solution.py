"""
QUESTION:
Write a function that creates a deep copy of the input list using the `copy` module in Python. The input list can be a multi-dimensional list containing integers and/or strings. The function should return the deep copy of the input list without modifying the original list. The function name should be `deep_copy_list`.
"""

import copy

def deep_copy_list(input_list):
    """
    This function creates a deep copy of the input list using the copy module in Python.
    
    Args:
    input_list (list): A multi-dimensional list containing integers and/or strings.

    Returns:
    list: A deep copy of the input list.
    """
    return copy.deepcopy(input_list)