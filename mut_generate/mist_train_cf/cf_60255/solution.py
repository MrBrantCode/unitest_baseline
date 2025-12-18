"""
QUESTION:
Write a function `rotate_matrix` that takes a 2D matrix and a rotation angle (90, 180, 270, or 360 degrees) as inputs and returns the rotated matrix in the clockwise direction. The rotation should be in-place without using extra space. Note that the function should be able to handle matrices of varying sizes.
"""

import numpy as np

def rotate_matrix(matrix, degree):
    """
    Rotate a 2D matrix by a given angle (90, 180, 270, or 360 degrees) in the clockwise direction.
    
    Args:
        matrix (list of lists): A 2D matrix to be rotated.
        degree (int): The rotation angle in degrees.

    Returns:
        numpy.ndarray: The rotated matrix.
    """
    rotation_functions = {
        90: lambda matrix: np.rot90(matrix, -1),
        180: lambda matrix: np.rot90(matrix, -2),
        270: lambda matrix: np.rot90(matrix, -3),
        360: lambda matrix: matrix
    }
    
    return rotation_functions[degree](np.array(matrix))