"""
QUESTION:
Create a function `calculate_polynomial_regression` that takes in a list of polynomial coefficients `p_coeff` and a list of dates, and returns the polynomial regression function and the first date in the list. The function should be able to handle a list of polynomial coefficients of any degree, where the coefficients are ordered from highest to lowest degree. The dates can be in any format, but the first date in the list should be returned as is.
"""

import numpy as np

def calculate_polynomial_regression(p_coeff, dates):
    poly = np.poly1d(p_coeff)  
    return poly, dates[0] 