"""
QUESTION:
Write a function `generate_permutations` that takes a list of distinct characters as input and returns all unique permutations of the characters. The function should return a list of lists, where each sublist is a permutation of the input characters.
"""

import itertools

def generate_permutations(chars):
    """
    Generate all unique permutations of the input characters.

    Args:
        chars (list): A list of distinct characters.

    Returns:
        list: A list of lists, where each sublist is a permutation of the input characters.
    """
    return [list(p) for p in itertools.permutations(chars)]