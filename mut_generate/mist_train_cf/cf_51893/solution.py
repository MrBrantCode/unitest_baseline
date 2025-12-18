"""
QUESTION:
Construct a function `calc_deriv` that takes in a list of polynomial coefficients `poly_coeffs` in descending order of degree and a NumPy array of x-values `x_values`. The function should return two NumPy arrays: `y_values` representing the polynomial function evaluated at `x_values`, and `derivative` representing the derivative of the polynomial function at `x_values` calculated using numerical differentiation with a small delta. The delta value should be a parameter with a default value of 1e-7.
"""

import numpy as np

def calc_deriv(poly_coeffs, x_values, delta=1e-7):
    """
    Evaluates a polynomial at given x-values and calculates its derivative using numerical differentiation.

    Args:
    poly_coeffs (list): Polynomial coefficients in descending order of degree.
    x_values (numpy array): X-values at which to evaluate the polynomial and calculate the derivative.
    delta (float, optional): Small value used for numerical differentiation. Defaults to 1e-7.

    Returns:
    tuple: A tuple containing the polynomial values (y_values) and the derivative values.
    """

    # Construct polynomial
    y_values = np.polyval(poly_coeffs, x_values)

    # Calculate derivative using numerical differentiation
    y_values_shifted = np.polyval(poly_coeffs, x_values + delta)
    derivative = (y_values_shifted - y_values) / delta

    return y_values, derivative