"""
QUESTION:
Write a function `add_positive_integer` that adds a new element to an array of integers. The element must be a positive integer and the array can only contain a maximum of 10 elements.
"""

def add_positive_integer(arr, element):
    """
    Adds a new positive integer element to an array if it has less than 10 elements.

    Args:
        arr (list): The array of integers.
        element (int): The positive integer to be added.

    Returns:
        bool: True if the element is added, False otherwise.
    """
    if element > 0 and len(arr) < 10:
        arr.append(element)
        return True
    else:
        return False