"""
QUESTION:
Create a function named `compute_poly` that takes a single float input `x` and returns the result of the polynomial expression 3x^3 + 4x - 2. Use the `numpy` library for the power operation.
"""

import numpy as np

def compute_poly(x):
    return 3 * np.power(x, 3) + 4 * x - 2