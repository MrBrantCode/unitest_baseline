"""
QUESTION:
Write a function `find_permutations` that generates all unique permutations of a given list of characters. The function should take a list of characters as input and return all possible permutations. The order of the permutations does not matter.
"""

import itertools

def find_permutations(chars):
    """
    Generates all unique permutations of a given list of characters.
    
    Args:
        chars (list): A list of characters.
    
    Returns:
        list: A list of tuples representing all possible permutations.
    """
    return list(itertools.permutations(chars))