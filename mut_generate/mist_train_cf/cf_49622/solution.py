"""
QUESTION:
Write a function `arrange_chars` that takes a list of unique characters as input and returns all unique possible arrangements of these characters.

The input list will contain at least one character, and the function should return a list of tuples, where each tuple represents a unique arrangement. The order of arrangements in the output list does not matter.
"""

import itertools

def arrange_chars(chars):
    """
    Returns all unique possible arrangements of the given list of characters.

    Args:
        chars (list): A list of unique characters.

    Returns:
        list: A list of tuples, where each tuple represents a unique arrangement.
    """
    return list(itertools.permutations(chars))