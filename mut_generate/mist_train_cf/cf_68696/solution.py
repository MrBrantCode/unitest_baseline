"""
QUESTION:
Construct a function `best_fit_polynomial` that takes in two lists of numbers `x_points` and `y_points` and an integer `degree`, and returns the polynomial equation that best fits the given dataset. The function should use NumPy's `polyfit` method to find the coefficients of the polynomial that minimizes the square error. The function should also be able to handle polynomials of any degree, where the degree is specified by the `degree` parameter.
"""

import numpy as np

def best_fit_polynomial(x_points, y_points, degree):
    """
    Construct the polynomial equation that best fits the given dataset.

    Parameters:
    x_points (list): List of x points.
    y_points (list): List of y points.
    degree (int): The degree of the polynomial.

    Returns:
    polynomial (numpy.poly1d): The polynomial equation that best fits the given dataset.
    """
    coefficients = np.polyfit(x_points, y_points, degree)
    polynomial = np.poly1d(coefficients)
    return polynomial