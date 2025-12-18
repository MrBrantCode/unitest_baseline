"""
QUESTION:
Create a function called `multiply_poly` that takes two lists of integers representing coefficients of polynomials as input. The function should return the coefficients of the resulting polynomial when the two input polynomials are multiplied together. The lengths of the input lists do not need to be equal.
"""

import numpy as np

def multiply_poly(p1, p2):
    """
    This function takes two lists of integers representing coefficients of polynomials as input.
    It returns the coefficients of the resulting polynomial when the two input polynomials are multiplied together.

    Parameters:
    p1 (list): coefficients of the first polynomial
    p2 (list): coefficients of the second polynomial

    Returns:
    list: coefficients of the resulting polynomial
    """
    return np.polymul(p1, p2)