"""
QUESTION:
Write a function called `find_roots` that calculates the roots of a polynomial equation given its coefficients. The coefficients should be passed as a list in descending order of powers, and the function should return the roots of the equation. The function should be able to handle polynomials of any degree and may use numerical methods or libraries to find the roots.
"""

import numpy as np

def find_roots(coefficients):
    """
    Calculate the roots of a polynomial equation given its coefficients.

    Parameters:
    coefficients (list): The coefficients of the polynomial in descending order of powers.

    Returns:
    roots (list): The roots of the equation.
    """
    return np.roots(coefficients)