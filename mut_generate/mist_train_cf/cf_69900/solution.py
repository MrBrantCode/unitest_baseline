"""
QUESTION:
Implement a function to demonstrate shallow copying and deep copying in Python, showing how each methodology handles nested objects and discussing the implications on memory allocation and performance. 

The function should take a list containing a nested list as input and return the original and copied lists after modification of the nested list in the copied list. Consider the memory allocation and performance implications of each copying method.
"""

import copy

def shallow_deep_copy(list1):
    """
    Demonstrates shallow and deep copying in Python.
    
    Args:
        list1 (list): A list containing a nested list.
    
    Returns:
        tuple: A tuple containing the original list, shallow-copied list, and deep-copied list after modification.
    """
    # Shallow Copy
    list_shallow = copy.copy(list1)
    list_shallow[2][0] = 'A'

    # Deep Copy
    list_deep = copy.deepcopy(list1)
    list_deep[2][0] = 'B'

    return list1, list_shallow, list_deep