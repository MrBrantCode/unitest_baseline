"""
QUESTION:
Create a function named `copy_data_structure` that demonstrates shallow and deep copying in Python, explaining the differences between these two methodologies in terms of memory usage and performance. The function should take a nested list, set, or dictionary as input and return the original data structure, a shallow copy, and a deep copy.
"""

import copy

def copy_data_structure(original_data):
    """
    This function demonstrates shallow and deep copying in Python.
    
    Args:
    original_data: A nested list, set, or dictionary.
    
    Returns:
    A tuple containing the original data structure, a shallow copy, and a deep copy.
    """
    
    # Create a shallow copy
    shallow_copied_data = copy.copy(original_data)
    
    # Create a deep copy
    deep_copied_data = copy.deepcopy(original_data)
    
    # Return the original data structure, a shallow copy, and a deep copy
    return original_data, shallow_copied_data, deep_copied_data