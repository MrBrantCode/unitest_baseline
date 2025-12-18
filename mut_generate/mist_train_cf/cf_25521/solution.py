"""
QUESTION:
Write a function `generate_permutations` that takes a list of elements as input and returns all possible permutations of the list. The function should return a list of tuples, where each tuple is a unique permutation of the input list. The order of the permutations does not matter.
"""

from itertools import permutations

def generate_permutations(my_list):
    """
    This function generates all possible permutations of a given list.
    
    Args:
        my_list (list): The input list of elements.
    
    Returns:
        list: A list of tuples, where each tuple is a unique permutation of the input list.
    """
    return list(permutations(my_list))