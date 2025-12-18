"""
QUESTION:
Write a function named `excise_element_from_tuple` that takes a tuple and an element as input, and returns a new tuple with the specified element removed. The function should work around the immutability of tuples in Python.
"""

def excise_element_from_tuple(tup, element):
    """
    Creates a new tuple with the specified element removed from the original tuple.
    
    Args:
    tup (tuple): The original tuple.
    element: The element to be removed.
    
    Returns:
    tuple: A new tuple with the specified element removed.
    """
    return tuple([x for x in tup if x != element])