"""
QUESTION:
Implement a function `copy_list` that creates a copy of a given list. The function should take a boolean argument `deep` to decide whether to create a shallow copy or a deep copy of the list. The function should return the copied list. The input list can be a nested list containing elements of any type, including other lists and mutable objects.
"""

import copy

def copy_list(input_list, deep=False):
    """
    Creates a copy of a given list.

    Args:
        input_list (list): The list to be copied.
        deep (bool): Whether to create a deep copy or a shallow copy. Defaults to False.

    Returns:
        list: The copied list.
    """
    if deep:
        return copy.deepcopy(input_list)
    else:
        return copy.copy(input_list)