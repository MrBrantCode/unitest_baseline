"""
QUESTION:
Write a function named `vectorized_addition` that takes two lists of integers as input, converts them into NumPy arrays, and returns their element-wise sum using vectorized addition. The function should not include any loops and should utilize the optimized performance of NumPy operations.
"""

import numpy as np

def vectorized_addition(a, b):
    """
    This function performs element-wise addition of two lists using NumPy arrays.
    
    Args:
        a (list): The first list of integers.
        b (list): The second list of integers.
    
    Returns:
        np.ndarray: A NumPy array representing the element-wise sum of the input lists.
    """
    return np.array(a) + np.array(b)