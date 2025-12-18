"""
QUESTION:
Write a function `f_double_prime` that calculates the value of the second derivative of a given function `f(x)` at `x=0.5` using numerical methods. The function `f(x)` is defined by a table of values, and the second derivative should be calculated by first finding the first derivative and then finding its rate of change with respect to `x`. The function should use a central difference method for the calculations and allow for a variable step size `h`.
"""

import numpy as np

# Define function f(x) from the given table
def f(x):
    x_values = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
    f_values = np.array([5.3, 3.1, 1.5, 0.9, 0.5, 0.3])
    return np.interp(x, x_values, f_values)

# Calculate the second derivative of f(x) using a central difference method
def f_double_prime(x, h=1e-6):
    return (f(x+h) - 2*f(x) + f(x-h)) / (h**2)