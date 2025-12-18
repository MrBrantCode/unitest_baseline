"""
QUESTION:
Create a function `manipulate_5d_array` that takes two 5-dimensional arrays of size 5x5x5x5x5 as input and returns the results of element-wise addition, subtraction, and multiplication operations between the two arrays. The function should utilize the numpy library.
"""

import numpy as np

def manipulate_5d_array(arr1, arr2):
    """
    This function performs element-wise addition, subtraction, and multiplication 
    operations on two 5-dimensional arrays of size 5x5x5x5x5.

    Args:
        arr1 (numpy.ndarray): The first 5D array.
        arr2 (numpy.ndarray): The second 5D array.

    Returns:
        tuple: A tuple containing the results of element-wise addition, subtraction, 
        and multiplication operations.
    """
    # Addition
    arr_add = np.add(arr1, arr2)
    
    # Subtraction
    arr_sub = np.subtract(arr1, arr2)
    
    # Multiplication
    arr_mul = np.multiply(arr1, arr2)
    
    return arr_add, arr_sub, arr_mul