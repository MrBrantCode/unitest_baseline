"""
QUESTION:
Write a function `filter_integers` that takes a list of values as input and returns a list containing only the integer values from the input list. The input list can contain values of any type, including integers, floats, strings, and other types. The function should return a list of integers, excluding all non-integer values.
"""

def filter_integers(lst):
    """
    This function filters a list to include only the integer values.

    Args:
        lst (list): A list containing values of any type.

    Returns:
        list: A list of integers.
    """
    return [i for i in lst if isinstance(i, int)]