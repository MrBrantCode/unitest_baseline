"""
QUESTION:
Write a function `shallow_copy` to create a shallow copy of an object. The function should retain the key characteristics of the original object while minimizing any potential issues. The object to be copied can be a list or a dictionary.
"""

import copy

def shallow_copy(obj):
    """
    Creates a shallow copy of the given object.
    
    Args:
        obj: The object to be copied. It can be a list or a dictionary.
    
    Returns:
        A shallow copy of the object.
    """
    if isinstance(obj, list):
        # Using slicing technique for lists
        return obj[:]
    elif isinstance(obj, dict):
        # Using the copy method for dictionaries
        return obj.copy()
    else:
        # Using the in-built Python function copy() for other objects
        return copy.copy(obj)