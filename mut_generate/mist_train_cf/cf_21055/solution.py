"""
QUESTION:
Write a function `generate_combinations` that generates all possible combinations of a given string where each combination contains exactly the same number of characters as the input string. The function should return a list of all combinations.
"""

from itertools import permutations

def generate_combinations(s):
    """
    Generates all possible combinations of a given string where each combination contains 
    exactly the same number of characters as the input string.

    Args:
    s (str): The input string.

    Returns:
    list: A list of all combinations.
    """
    return [''.join(p) for p in permutations(s)]