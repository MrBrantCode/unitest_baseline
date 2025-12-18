"""
QUESTION:
Write a function named `vectorized_addition` that takes two lists of integers as input and returns a list of their corresponding sums. The function should use vectorization to achieve optimal performance. The input lists are guaranteed to have the same length.
"""

import numpy as np

def vectorized_addition(a, b):
    """
    This function takes two lists of integers as input, converts them into NumPy arrays, 
    and returns a list of their corresponding sums using vectorized addition.

    Args:
        a (list): The first list of integers.
        b (list): The second list of integers.

    Returns:
        list: A list of the corresponding sums of the input lists.
    """
    return (np.array(a) + np.array(b)).tolist()