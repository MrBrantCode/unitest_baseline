"""
QUESTION:
Create a function `perform_operations` that takes two 5D arrays of dimensions 5 x 5 x 5 x 5 x 5 as input and returns the results of element-wise addition, subtraction, and multiplication of the two arrays. The function should use NumPy to handle the arrays.
"""

import numpy as np

def perform_operations(array1, array2):
    """
    This function takes two 5D arrays as input and returns the results of element-wise addition, subtraction, and multiplication of the two arrays.

    Parameters:
    array1 (numpy array): The first 5D array.
    array2 (numpy array): The second 5D array.

    Returns:
    A tuple containing the results of element-wise addition, subtraction, and multiplication.
    """
    addition = np.add(array1, array2)
    subtraction = np.subtract(array1, array2)
    multiplication = np.multiply(array1, array2)
    
    return addition, subtraction, multiplication