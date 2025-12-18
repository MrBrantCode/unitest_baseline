"""
QUESTION:
Write a function called `calculate_product` to calculate the product of all elements in a three-dimensional array. The function should take a 3D array as input and return the product of all its elements. The array can contain any integers.
"""

import numpy as np

def calculate_product(arr):
    """
    Calculate the product of all elements in a three-dimensional array.
    
    Args:
        arr (numpy.ndarray): A 3D array containing integers.
    
    Returns:
        int: The product of all elements in the array.
    """
    return np.prod(arr)