"""
QUESTION:
Given a list of integers, write a function `find_even_indices` that returns a list of indices of the even numbers in the given list.
"""

def find_even_indices(array):
    """
    Returns a list of indices of the even numbers in the given list.

    Args:
        array (list): A list of integers.

    Returns:
        list: A list of indices of the even numbers.
    """
    return [i for i, x in enumerate(array) if x % 2 == 0]