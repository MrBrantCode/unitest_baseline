"""
QUESTION:
Create a function called `create_copy` to demonstrate the difference between shallow copy and deep copy. The function should take two arguments: the original object to be copied and a boolean indicating whether to create a shallow copy or a deep copy. The function should return the copied object.
"""

import copy

def create_copy(obj, is_deep_copy):
    """
    Creates a copy of the given object.

    Args:
    obj (object): The object to be copied.
    is_deep_copy (bool): A boolean indicating whether to create a deep copy or a shallow copy.

    Returns:
    object: The copied object.
    """
    if is_deep_copy:
        return copy.deepcopy(obj)
    else:
        return copy.copy(obj)