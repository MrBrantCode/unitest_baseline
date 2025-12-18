"""
QUESTION:
Create a function called `get_permutations` that takes two lists of integers, `list1` and `list2`, as input and returns a list of tuples. Each tuple in the output list should represent a unique permutation resulting from combining one element from `list1` with one element from `list2`. The function should not use any external libraries beyond the Python standard library.
"""

import itertools

def get_permutations(list1, list2):
    """
    Returns a list of tuples, each representing a unique permutation 
    resulting from combining one element from list1 with one element from list2.
    
    Args:
        list1 (list): The first list of integers.
        list2 (list): The second list of integers.
    
    Returns:
        list: A list of tuples, each tuple containing one element from list1 and one element from list2.
    """
    return list(itertools.product(list1, list2))