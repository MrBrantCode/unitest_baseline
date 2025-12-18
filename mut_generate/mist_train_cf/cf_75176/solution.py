"""
QUESTION:
Write a function called `cartesian_product` that takes two lists as input and returns their Cartesian product, i.e., all possible pairs of elements from the two lists. The function should use the `itertools.product` function.
"""

import itertools

def cartesian_product(list1, list2):
    """
    Returns the Cartesian product of two lists.
    
    Args:
        list1 (list): The first list.
        list2 (list): The second list.
    
    Returns:
        list: A list of tuples, where each tuple is a pair of elements from the two input lists.
    """
    return list(itertools.product(list1, list2))