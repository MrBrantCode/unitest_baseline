"""
QUESTION:
Write a function to generate all possible permutations of a given list of strings. The function should accept a list of strings as input and return all possible permutations of the input strings.
"""

from itertools import permutations

def generate_permutations(strings):
    """
    Generate all possible permutations of a given list of strings.

    Args:
    strings (list): A list of strings.

    Returns:
    permutations: An iterable that yields tuples of all permutations.
    """
    return permutations(strings)