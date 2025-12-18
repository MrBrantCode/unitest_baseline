"""
QUESTION:
Create a function named `series_to_matrix` that takes a one-dimensional series of integers as input and returns a three-dimensional matrix. The function should reshape the input series into a 2x3x1 three-dimensional matrix. The input series is not guaranteed to have a length that is a multiple of 6, so the function should be able to handle this case. Use numpy library for numerical and matrix computations.
"""

import numpy as np

def series_to_matrix(series):
    """
    Reshapes a one-dimensional series of integers into a three-dimensional matrix.
    
    Args:
    series (numpy.array): A one-dimensional series of integers.
    
    Returns:
    numpy.ndarray: A 2x3x1 three-dimensional matrix.
    """
    return series.reshape(2, 3, 1)