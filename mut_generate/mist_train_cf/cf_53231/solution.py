"""
QUESTION:
Write a function called `calculate_corr_coef(x, y)` that calculates the correlation coefficient between two variables `x` and `y`. The function should take in two lists `x` and `y` as input and return the correlation coefficient as a float. The function should use the numpy library to calculate the correlation coefficient.
"""

import numpy as np

def calculate_corr_coef(x, y):
    return np.corrcoef(x, y)[0, 1]