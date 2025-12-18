"""
QUESTION:
Create functions for 2D transformations. Implement the `Rotate`, `Translate`, and `Scale` functions to return 2D rotation, translation, and scaling matrices respectively. The `Rotate` function takes an angle in radians as input. The `Translate` function takes a tuple representing the translation vector as input. The `Scale` function takes a scaling factor as input. Apply these transformations to a 2D shape in the order: rotation, translation, and scaling. Write the resulting 3x3 transformation matrix to a file named "matrix_fun.ipe" in the Ipe format.

Restrictions: The output file should be in the Ipe format, with the transformation matrix written as a 3x3 matrix in the file.
"""

import numpy as np

def rotate(angle):
    return np.array([[np.cos(angle), -np.sin(angle), 0], [np.sin(angle), np.cos(angle), 0], [0, 0, 1]])

def translate(translation):
    return np.array([[1, 0, translation[0]], [0, 1, translation[1]], [0, 0, 1]])

def scale(factor):
    return np.array([[factor, 0, 0], [0, factor, 0], [0, 0, 1]])