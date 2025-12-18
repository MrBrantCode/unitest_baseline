"""
QUESTION:
Write a function called `modify_tuple` to add a new element to a given tuple. The function should take a tuple and an element as input and return a new tuple with the element added. The original tuple should remain unchanged.
"""

def modify_tuple(tup, element):
    """
    This function adds a new element to a given tuple.

    Args:
        tup (tuple): The input tuple.
        element: The element to be added to the tuple.

    Returns:
        tuple: A new tuple with the element added.
    """
    return tup + (element,)