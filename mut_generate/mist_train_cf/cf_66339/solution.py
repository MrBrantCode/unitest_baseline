"""
QUESTION:
Implement a function called `insert_at_start` that takes a tuple and an element as input, and returns a new tuple with the element inserted at the start of the original tuple. The original tuple should not be modified.
"""

def insert_at_start(original_tuple, element):
    """
    Inserts an element at the start of a tuple.

    Args:
        original_tuple (tuple): The original tuple to be modified.
        element: The element to be inserted.

    Returns:
        tuple: A new tuple with the element inserted at the start.
    """
    list_version = list(original_tuple)
    list_version.insert(0, element)
    return tuple(list_version)