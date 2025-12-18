"""
QUESTION:
Implement a function `ridge_regression_gradient(X, w, y, lambda_val)` that calculates the gradient of the function `0.5 * ||Xw-y||^2 + 0.5 * lambda_val * ||w||^2` with respect to `w`, where `X` is the input data matrix, `y` is the target vector, `w` is the weight vector, and `lambda_val` is a non-negative regularization parameter. The function should return the gradient vector.
"""

import numpy as np

def ridge_regression_gradient(X, w, y, lambda_val):
    """
    This function calculates the gradient of the function 
    0.5 * ||Xw-y||^2 + 0.5 * lambda_val * ||w||^2 with respect to w.

    Parameters:
    X (numpy array): input data matrix
    w (numpy array): weight vector
    y (numpy array): target vector
    lambda_val (float): non-negative regularization parameter

    Returns:
    numpy array: the gradient vector
    """
    return X.T @ (X @ w - y) + lambda_val * w