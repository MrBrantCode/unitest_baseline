"""
QUESTION:
Write a function `compute_permutations` that takes an array as input and returns all possible unique arrangement combinations for its elements. The function should not use recursion.
"""

from itertools import permutations

def compute_permutations(array):
    """
    Compute all possible unique arrangement combinations for the elements in the input array.
    
    Args:
    array (list): The input array of elements.
    
    Returns:
    list: A list of tuples, each representing a unique permutation of the input array.
    """
    return list(permutations(array))