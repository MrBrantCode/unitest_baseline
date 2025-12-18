"""
QUESTION:
Write a function `find_cubic_roots` that determines the zeroes of a cubic polynomial equation of the form ax^3 + bx^2 + cx + d = 0, where a = 1, b = -4, c = 3, and d = -2. The function should return all roots, including complex numbers if applicable.
"""

import numpy as np

def find_cubic_roots(a, b, c, d):
    """
    Find the roots of a cubic polynomial equation of the form ax^3 + bx^2 + cx + d = 0.

    Args:
    a (float): Coefficient of the cubic term.
    b (float): Coefficient of the quadratic term.
    c (float): Coefficient of the linear term.
    d (float): Constant term.

    Returns:
    list: A list of roots of the polynomial equation.
    """
    return np.roots([a, b, c, d])