"""
QUESTION:
Generate all possible permutations of a list of integers with length `n` using the Python `itertools` module, ensuring no elements are repeated, and store them in a list. The function should take a list of integers as input and return a list of tuples, each representing a permutation of the input list.
"""

from itertools import permutations

def generate_permutations(int_list):
    """
    Generate all possible permutations of a list of integers with length n.
    
    Args:
    int_list (list): A list of integers.
    
    Returns:
    list: A list of tuples, each representing a permutation of the input list.
    """
    return list(permutations(int_list))