"""
QUESTION:
Write a function `create_matrix` that takes a sequence of numerical values as input and returns a three-dimensional matrix with shape (2, 2, n), where n is determined by the length of the sequence. The function should raise a ValueError if the total number of elements does not match the desired shape.
"""

import numpy as np

def create_matrix(sequence):
    """
    This function takes a sequence of numerical values as input and returns a three-dimensional matrix with shape (2, 2, n), 
    where n is determined by the length of the sequence. The function raises a ValueError if the total number of elements does not match the desired shape.

    Args:
        sequence (list): A list of numerical values.

    Returns:
        np.ndarray: A 3D NumPy array.
    """
    return np.array(sequence).reshape(2, 2, -1)