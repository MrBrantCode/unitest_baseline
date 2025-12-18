"""
QUESTION:
Create a function called `create_shallow_copy` that creates a shallow copy of a given object. The function should take one argument, the object to be copied. The function should return a new object that is a shallow copy of the original object, meaning it copies the object's references to other objects.
"""

import copy

def create_shallow_copy(obj):
    """
    Creates a shallow copy of a given object.
    
    Args:
        obj: The object to be copied.
    
    Returns:
        A new object that is a shallow copy of the original object.
    """
    return copy.copy(obj)