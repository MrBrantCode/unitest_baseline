"""
QUESTION:
Implement the `finite_difference_gradient` function, which takes in a Python function `f`, a NumPy array `x` of shape `(n_params, n_train)`, and a float `h`, and returns a NumPy array representing the gradient of `f` with respect to the input parameters at the points specified by `x`. The function `f` takes in a NumPy array of shape `(n_params, n_train)` and returns a NumPy array of shape `(1, n_train)`. Use the central finite difference method to calculate the gradient. The step size for the finite difference method is given by `h`.
"""

import numpy as np

def finite_difference_gradient(f, x, h):
    n_params, n_train = x.shape
    grad = np.zeros((n_params, n_train))

    for i in range(n_params):
        x_plus_h = x.copy()
        x_plus_h[i] += h
        x_minus_h = x.copy()
        x_minus_h[i] -= h
        grad[i] = (f(x_plus_h) - f(x_minus_h)) / (2 * h)

    return grad