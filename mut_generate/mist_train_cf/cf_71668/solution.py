"""
QUESTION:
Flip a 2D numpy array diagonally from top left to bottom right using the `transpose` function.
"""

import numpy as np

def flip_diagonally(arr):
    """
    Flip a 2D numpy array diagonally from top left to bottom right.

    Parameters:
    arr (numpy.ndarray): The input 2D numpy array.

    Returns:
    numpy.ndarray: The flipped array.
    """
    return np.transpose(arr)