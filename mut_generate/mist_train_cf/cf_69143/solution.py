"""
QUESTION:
Generate all unique permutations of a list of words. The function should take a list of words as input and return all possible orderings of the words. The permutations should be returned as a list of tuples, with each tuple representing a unique ordering of the input words.
"""

import itertools

def generate_permutations(words):
    """
    Generate all unique permutations of a list of words.
    
    Args:
        words (list): A list of words.
    
    Returns:
        list: A list of tuples, each representing a unique ordering of the input words.
    """
    return list(itertools.permutations(words))