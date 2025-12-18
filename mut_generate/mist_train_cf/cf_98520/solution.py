"""
QUESTION:
Write a function `improve_nested_loops` that takes two lists of integers as input and returns the Cartesian product of the lists, as well as the common elements between the two lists. The function should use the itertools module to improve code efficiency. The input lists can be large, and the function should be able to handle them efficiently.
"""

import itertools

def improve_nested_loops(list1, list2):
    """
    This function calculates the Cartesian product of two lists and finds the common elements between them.
    
    Parameters:
    list1 (list): The first list of integers.
    list2 (list): The second list of integers.
    
    Returns:
    tuple: A tuple containing the Cartesian product and the common elements.
    """
    
    # Calculate the Cartesian product of the two lists
    cartesian_product = list(itertools.product(list1, list2))
    
    # Find the common elements between the two lists
    common_elements = list(set(list1) & set(list2))
    
    return cartesian_product, common_elements