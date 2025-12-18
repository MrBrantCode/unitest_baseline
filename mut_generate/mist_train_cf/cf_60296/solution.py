"""
QUESTION:
Write a function named `solve_poly` that accepts the coefficients of a polynomial equation as a list, where the coefficients are ordered from the highest degree to the lowest degree. The function should return the roots of the polynomial equation, handling both real and complex roots.
"""

import numpy as np

def solve_poly(coefficients):
    roots = np.roots(coefficients)
    real_roots = [root.real if abs(root.imag) < 1e-5 else root for root in roots]
    return real_roots