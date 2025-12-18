"""
QUESTION:
Implement the `transform_array` function, which takes an input array of two numbers [x, y] and returns a new array [x^2 * y, 5x + sin(y)].
"""

import numpy as np

def transform_array(input_array):
    x, y = input_array
    transformed_x = x**2 * y
    transformed_y = 5 * x + np.sin(y)
    return np.array([transformed_x, transformed_y])