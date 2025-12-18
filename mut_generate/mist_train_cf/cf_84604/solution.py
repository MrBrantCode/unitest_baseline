"""
QUESTION:
Write a function to get the diagonal elements of a square numpy array starting from the upper right to the lower left. The function should be general and work for arrays of varying shapes, not just 5x5. The function should take a 2D numpy array as input and return a 1D numpy array containing the diagonal elements.
"""

import numpy as np

def get_diagonal_elements(a):
    """
    This function takes a 2D numpy array as input and returns a 1D numpy array containing the diagonal elements 
    starting from the upper right to the lower left.

    Parameters:
    a (numpy array): A 2D numpy array.

    Returns:
    numpy array: A 1D numpy array containing the diagonal elements.
    """
    return np.fliplr(a).diagonal()