"""
QUESTION:
Write a function `linear_regression` that takes two lists of numbers `X` and `Y` as input and returns the slope and y-intercept of the linear regression line using the least squares method. The function should not take any additional arguments.
"""

import numpy as np

def linear_regression(X, Y):
    n = len(X)
    sum_x = np.sum(X)
    sum_y = np.sum(Y)
    sum_x_squared = np.sum(X**2)
    sum_xy = np.sum(X*Y)

    b1_numerator = (n * sum_xy) - (sum_x * sum_y)
    b1_denominator = (n * sum_x_squared) - (sum_x**2)
    b1 = b1_numerator / b1_denominator

    b0 = (sum_y - (b1 * sum_x)) / n

    return b0, b1