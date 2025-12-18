"""
QUESTION:
Write a function called `generate_combinations` that generates all combinations of a given string where each combination contains exactly `n` characters, without using recursion, and returns these combinations as a list of strings. The function should take two parameters: a string `s` and an integer `n`, which represents the length of each combination.
"""

import itertools

def generate_combinations(s, n):
    """
    Generate all combinations of a given string where each combination contains exactly n characters.

    Args:
        s (str): The input string.
        n (int): The length of each combination.

    Returns:
        list: A list of strings, each representing a combination of the input string.
    """
    return [''.join(p) for p in itertools.product(s, repeat=n)]