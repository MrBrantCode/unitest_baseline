"""
QUESTION:
Implement a function named `create_copy` that creates a copy of a given list. The function should take two parameters: `original_list` and `deep`. If `deep` is `True`, the function should create a deep copy of the list; otherwise, it should create a shallow copy. The function should return the copied list. 

Restrictions: 
- The function should use the `copy` module.
- The function should handle nested lists.
"""

import copy

def create_copy(original_list, deep):
    """
    Creates a copy of a given list.

    Args:
        original_list (list): The list to be copied.
        deep (bool): Whether to create a deep copy or a shallow copy.

    Returns:
        list: The copied list.
    """
    if deep:
        return copy.deepcopy(original_list)
    else:
        return copy.copy(original_list)