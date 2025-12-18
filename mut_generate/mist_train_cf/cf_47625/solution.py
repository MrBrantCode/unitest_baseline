"""
QUESTION:
Write a function `product_of_elements` that takes a three-dimensional array as input, calculates the product of elements in each sub-array (excluding those containing zero), and returns the results in descending order. The function should handle cases where some elements in the sub-arrays are zero.
"""

import numpy as np

def product_of_elements(arr):
    """
    This function calculates the product of elements in each sub-array 
    (excluding those containing zero) in a three-dimensional array and 
    returns the results in descending order.

    Parameters:
    arr (list): A three-dimensional array of integers.

    Returns:
    list: A list of products in descending order.
    """
    result = []
    
    for two_d in arr:
        for one_d in two_d:
            if 0 not in one_d:
                result.append(np.prod(one_d))
                
    result.sort(reverse=True)
    
    return result