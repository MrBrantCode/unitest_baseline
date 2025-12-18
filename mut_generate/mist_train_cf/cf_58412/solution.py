"""
QUESTION:
Write a Python function named 'permutations' that takes a list of elements and an integer as input, and returns all permutations of the list taking the specified number of elements at a time. The function should use the itertools module and return an iterable.
"""

from itertools import permutations

def permutations(lst, n):
    """
    Returns all permutations of the list taking the specified number of elements at a time.

    Args:
        lst (list): The input list of elements.
        n (int): The number of elements to take at a time.

    Returns:
        iterable: An iterable of tuples, each representing a permutation of the input list.
    """
    return permutations(lst, n)