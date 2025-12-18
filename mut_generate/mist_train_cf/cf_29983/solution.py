"""
QUESTION:
Implement the `polynomial_regression` function, which takes in three parameters: `x_values`, a list of x-coordinates of the data points; `y_values`, a list of y-coordinates of the data points; and `degree`, an integer representing the degree of the polynomial to be used for regression. The function should return a list of coefficients representing the polynomial that best fits the given data points. Assume that the input lists `x_values` and `y_values` are of the same length and contain at least `degree + 1` data points.
"""

import numpy as np

def polynomial_regression(x_values, y_values, degree):
    X = np.array([[x**d for d in range(degree+1)] for x in x_values])
    Y = np.array(y_values)
    coeffs = np.linalg.inv(X.T @ X) @ X.T @ Y
    return coeffs.tolist()