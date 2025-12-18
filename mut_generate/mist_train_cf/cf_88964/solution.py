"""
QUESTION:
Write a function `copy_lists` that takes a list `original_list` as an argument and returns two lists: a shallow copy and a deep copy of the `original_list`. The function should modify the nested list inside the shallow copy and the deep copy, and then return the original list, the shallow copy, and the deep copy. The function should use the `copy` module to create the shallow and deep copies.
"""

import copy

def copy_lists(original_list):
    """
    Creates shallow and deep copies of the original list, 
    modifies the nested lists, and returns the original list, 
    the shallow copy, and the deep copy.

    Args:
        original_list (list): The original list to be copied.

    Returns:
        tuple: A tuple containing the original list, the shallow copy, and the deep copy.
    """
    # Shallow copy
    shallow_copy = copy.copy(original_list)
    
    # Deep copy
    deep_copy = copy.deepcopy(original_list)
    
    # Modifying the nested list inside the shallow copy
    if isinstance(shallow_copy, list) and len(shallow_copy) > 0 and isinstance(shallow_copy[-1], list):
        shallow_copy[2].append(5)
    
    # Modifying the nested list inside the deep copy
    if isinstance(deep_copy, list) and len(deep_copy) > 0 and isinstance(deep_copy[-1], list):
        deep_copy[2].append(6)
    
    return original_list, shallow_copy, deep_copy