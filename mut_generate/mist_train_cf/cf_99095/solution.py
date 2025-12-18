"""
QUESTION:
Write a function `non_linear_eq` that calculates the output of the non-linear equation y = sin(x) + x^2 - 5x. The function should take one argument `x` and return the calculated output `y`. The function should use the numpy library for mathematical operations.
"""

import numpy as np

def non_linear_eq(x):
    # Define a non-linear equation
    y = np.sin(x) + x**2 - 5*x
    return y