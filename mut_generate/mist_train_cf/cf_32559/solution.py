"""
QUESTION:
Implement a function `ucurve_fit` that takes a function `reg_cubic` and two arrays `x` and `y` as input, and returns the coefficients of the cubic polynomial that best fits the data points represented by `x` and `y`. The `reg_cubic` function is assumed to be implemented and provided, and it computes the regression matrix for a cubic polynomial given an array `x`. The `ucurve_fit` function should use the `reg_cubic` function to perform the cubic fit and return the coefficients.
"""

import numpy as np

def ucurve_fit(reg_cubic, x, y):
    X = reg_cubic(x)
    params = np.linalg.lstsq(X, y, rcond=None)[0]
    return params