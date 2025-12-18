"""
QUESTION:
Write a function `calculate_correlation` to compute the correlation between two arrays of numbers. The function should return the correlation coefficient, which is a unitless measurement that is not affected by linear transformations such as redefining measurement units or augmenting the same constant to every x-variable value. The correlation coefficient should also be symmetrical, meaning the correlation of x with y is the same as the correlation of y with x. The function should take two one-dimensional arrays `x` and `y` as input and return the correlation coefficient as output.
"""

import numpy as np

def calculate_correlation(x, y):
    """
    Compute the correlation between two arrays of numbers.

    Args:
        x (numpy array): The first array of numbers.
        y (numpy array): The second array of numbers.

    Returns:
        float: The correlation coefficient.
    """
    return np.corrcoef(x, y)[0,1]