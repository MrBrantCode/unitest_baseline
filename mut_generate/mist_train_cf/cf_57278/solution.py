"""
QUESTION:
Write a function named 'sortFloatingPointValues' that takes a list of floating-point numbers as input and returns the list sorted in ascending order. The function should be able to handle both positive and negative values, as well as duplicates, and should perform a stable sort.
"""

def sortFloatingPointValues(values):
    """
    Sorts a list of floating-point numbers in ascending order.

    Args:
    values (list): A list of floating-point numbers.

    Returns:
    list: The sorted list of floating-point numbers.
    """
    values.sort()
    return values