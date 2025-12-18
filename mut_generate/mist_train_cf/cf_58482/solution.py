"""
QUESTION:
Write a function `matrix_power` that raises a 2D square numpy array to an integer power `n` while maintaining its array format and avoiding conversion to matrix type. The function should take two inputs: a 2D square numpy array `A` and an integer `n`. The array `A` must have the same number of rows as columns. The output should be a 2D numpy array resulting from raising `A` to the power `n`.
"""

import numpy as np

def matrix_power(A, n):
    """
    Raises a 2D square numpy array to an integer power n while maintaining its array format.
    
    Args:
        A (numpy.ndarray): A 2D square numpy array.
        n (int): The power to which the array should be raised.
    
    Returns:
        numpy.ndarray: A 2D numpy array resulting from raising A to the power n.
    """
    return np.linalg.matrix_power(A, n)