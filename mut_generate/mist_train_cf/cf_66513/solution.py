"""
QUESTION:
Given a function $f(w) = \frac{1}{2} \norm{Xw-y}^2_2 + \frac{1}{2}\lambda \norm{w}^2_2$, calculate the gradient of $f(w)$ with respect to $w$, where $X$ is the design matrix, $y$ is the target vector, $w$ is the weight vector, and $\lambda$ is the regularization parameter.
"""

import numpy as np

def gradient_f_w(X, y, w, lambda_val):
    """
    Calculate the gradient of the regularized linear regression objective with respect to w.

    Args:
    X (numpy array): Design matrix
    y (numpy array): Target vector
    w (numpy array): Weight vector
    lambda_val (float): Regularization parameter

    Returns:
    numpy array: Gradient of the objective function with respect to w
    """
    return np.dot(X.T, np.dot(X, w) - y) + lambda_val * w