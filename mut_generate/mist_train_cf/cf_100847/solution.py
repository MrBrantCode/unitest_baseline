"""
QUESTION:
Write a function `cartesian_product` that calculates the Cartesian product of two lists and a function `common_elements` that finds the common elements between two lists, optimizing the solution using the itertools module and avoiding inefficiencies caused by nested for loops. The function should be able to handle large data sets efficiently.
"""

import itertools

def cartesian_product(list1, list2):
    """
    Calculate the Cartesian product of two lists.
    
    Args:
        list1 (list): The first list.
        list2 (list): The second list.
    
    Returns:
        list: A list of tuples representing the Cartesian product of the input lists.
    """
    return list(itertools.product(list1, list2))


def common_elements(list1, list2):
    """
    Find the common elements between two lists.
    
    Args:
        list1 (list): The first list.
        list2 (list): The second list.
    
    Returns:
        list: A list of common elements between the input lists.
    """
    return list(set(list1) & set(list2))