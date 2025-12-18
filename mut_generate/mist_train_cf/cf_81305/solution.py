"""
QUESTION:
Create a function that effectively implements a shallow copy of an object. Compare and discuss the difference between shallow and deep copy operations in Python, specifically their impact on mutable objects (e.g., lists and dictionaries) and immutable objects (e.g., strings). Note that the function should utilize the copy module in Python and handle both shallow and deep copy operations.
"""

import copy

def shallow_copy(obj):
    """
    Creates a shallow copy of the given object.

    Args:
    obj: The object to be copied.

    Returns:
    A shallow copy of the object.
    """
    return copy.copy(obj)