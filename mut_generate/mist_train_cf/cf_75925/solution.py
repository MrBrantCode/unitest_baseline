"""
QUESTION:
Create a function named `deep_copy_list` that takes a list as input and returns a deep copy of the list. The list may contain nested lists. The function should return a new list that is completely independent of the original list, meaning changes to the copied list will not affect the original list.
"""

import copy

def deep_copy_list(input_list):
    """
    Creates a deep copy of the input list.
    
    Args:
    input_list (list): The list to be copied.
    
    Returns:
    list: A deep copy of the input list.
    """
    return copy.deepcopy(input_list)