"""
QUESTION:
Create a function named `rotate_matrix` that takes a square matrix and a number of steps as input, and returns the matrix rotated to the right by the specified number of steps. Ensure that the rotation does not distort the original structure of the matrix. Note that steps greater than 4 are equivalent to their remainder when divided by 4, and the rotation should be performed in a layer-by-layer manner.
"""

import numpy as np

def rotate_matrix(matrix, steps):
    steps = steps % 4  # Converting steps greater than 4 to their equivalent steps within 4
    return np.rot90(matrix, -steps).tolist()