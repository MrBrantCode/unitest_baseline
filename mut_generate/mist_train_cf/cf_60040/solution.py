"""
QUESTION:
Write a function called `pad_matrices` that takes a 2D numpy array `matrix` and a target `dimension` as inputs, and returns the input `matrix` with a border of zeros added to match the target `dimension`. The border of zeros should be added symmetrically around the original matrix. Assume the target `dimension` is a tuple of two integers representing the desired height and width of the output matrix.
"""

import numpy as np

def pad_matrices(matrix, dimension):
    """
    Pads a 2D numpy array with a border of zeros to match the target dimension.
    
    Args:
    matrix (numpy array): The input 2D numpy array.
    dimension (tuple): A tuple of two integers representing the desired height and width of the output matrix.
    
    Returns:
    numpy array: The input matrix with a border of zeros added to match the target dimension.
    """
    return np.pad(matrix, ((0, dimension[0]-matrix.shape[0]), (0, dimension[1]-matrix.shape[1])), mode='constant')