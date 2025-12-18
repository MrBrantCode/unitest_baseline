"""
QUESTION:
Fit the equation y = A + Blogx to a dataset using NumPy's polyfit function. The function should take two parameters, x and y, which are 1D arrays of the same length, and return an np.array of [A, B]. The function should not have any additional parameters. 

Restriction: Use NumPy's polyfit function and do not use any built-in logarithmic or exponential fitting functions.
"""

import numpy as np

def entance(x, y):
    log_x = np.log(x)
    coef = np.polyfit(log_x, y, 1)
    return np.array([coef[1], coef[0]])