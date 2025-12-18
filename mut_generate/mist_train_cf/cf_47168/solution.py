"""
QUESTION:
Write a function `deep_or_shallow_copy` that creates a duplicate copy of a given object using either deep copying or shallow copying, depending on the type of the object's elements. If the object contains only immutable elements, use shallow copying; otherwise, use deep copying.
"""

import copy

def deep_or_shallow_copy(obj):
    """
    Creates a duplicate copy of a given object using either deep copying or shallow copying,
    depending on the type of the object's elements.

    If the object contains only immutable elements, use shallow copying; otherwise, use deep copying.

    Args:
        obj (object): The object to be copied.

    Returns:
        object: A copy of the input object.
    """
    # Check if the object is a list or a tuple
    if isinstance(obj, (list, tuple)):
        # Check if the object contains only immutable elements
        if all(isinstance(item, (int, float, str, tuple)) for item in obj):
            # Use shallow copying for objects with immutable elements
            return obj[:]
        else:
            # Use deep copying for objects with mutable elements
            return copy.deepcopy(obj)
    else:
        # For non-list or non-tuple objects, use deep copying
        return copy.deepcopy(obj)