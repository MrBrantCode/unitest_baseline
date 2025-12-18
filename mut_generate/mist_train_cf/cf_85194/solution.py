"""
QUESTION:
Compose a function named `fit_polynomial` in Python that takes two lists, `x_points` and `y_points`, representing x and y coordinates, and returns the coefficients of a polynomial that best fits the provided data points using the `polyfit` function from the `numpy` library. The function should allow the degree of the polynomial to be specified, defaulting to 1 if not provided, to accommodate both linear and higher degree polynomial fits.
"""

import numpy as np

def fit_polynomial(x_points, y_points, degree=1):
    """
    Fits a polynomial of a specified degree to the provided data points.

    Parameters:
    x_points (list): A list of x-coordinates.
    y_points (list): A list of y-coordinates.
    degree (int, optional): The degree of the polynomial. Defaults to 1.

    Returns:
    coefficients (list): The coefficients of the fitted polynomial.
    """
    coefficients = np.polyfit(x_points, y_points, degree)
    
    return coefficients