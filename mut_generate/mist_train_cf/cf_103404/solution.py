"""
QUESTION:
Create a function called `deep_copy` that creates a completely independent copy of a given nested list. The function should return a new list that has the same elements as the original list, but any changes made to the original list should not affect the copied list.
"""

import copy

def deep_copy(lst):
    """
    Creates a completely independent copy of a given nested list.
    
    Args:
    lst (list): The nested list to be copied.
    
    Returns:
    list: A new list that has the same elements as the original list.
    """
    return copy.deepcopy(lst)