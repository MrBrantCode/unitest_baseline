"""
QUESTION:
Generate all unique permutations of a list of integers using the Python itertools module. Implement a function `generate_permutations` that takes a list of integers as input and returns a list of tuples, where each tuple is a unique permutation of the input list. Assume that the input list contains unique integers.
"""

from itertools import permutations

def generate_permutations(int_list):
    """
    Generate all unique permutations of a list of integers.

    Args:
    int_list (list): A list of unique integers.

    Returns:
    list: A list of tuples, where each tuple is a unique permutation of the input list.
    """
    return list(permutations(int_list))