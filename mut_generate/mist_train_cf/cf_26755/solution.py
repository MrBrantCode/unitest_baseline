"""
QUESTION:
Implement a function named `jacobian` that takes a multivariate function `fun` as input and returns a new function that computes both the function value and its Jacobian at a given point. The Jacobian matrix should be computed using numerical differentiation with a step size of `1e-10`. The returned function should take a 1D NumPy array `x` as input and return the function value and the Jacobian matrix as a tuple. The function `fun` takes a 1D NumPy array `x` as input and returns a 1D NumPy array representing the function value at point `x`.
"""

import numpy as np

def jacobian(fun):
    def jacobian_func(x):
        h = 1e-10  # Small value for numerical differentiation
        n = len(x)
        J = np.zeros((len(fun(x)), n))  # Initialize Jacobian matrix

        for i in range(n):
            x_plus_h = x.copy()
            x_plus_h[i] += h
            J[:, i] = (fun(x_plus_h) - fun(x)) / h  # Compute the i-th column of the Jacobian

        return fun(x), J  # Return function value and Jacobian matrix

    return jacobian_func