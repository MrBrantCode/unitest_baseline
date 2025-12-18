"""
QUESTION:
Write a Python function `f_double_prime(x, h=1e-6)` that uses numerical methods to calculate the second derivative of a given function `f(x)` at a point `x`. The function `f(x)` is represented by a table of x and f(x) values. The function `f_double_prime(x, h=1e-6)` should use a central difference method with step size `h` to calculate the second derivative.
"""

import numpy as np

def f_double_prime(x, h=1e-6):
    x_values = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
    f_values = np.array([5.3, 3.1, 1.5, 0.9, 0.5, 0.3])
    f = lambda x: np.interp(x, x_values, f_values)
    return (f(x+h) - 2*f(x) + f(x-h)) / (h**2)