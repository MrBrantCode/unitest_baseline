"""
QUESTION:
Create a function called `non_linear_eq` that takes one argument `x` and returns the value of the equation `y = sin(x) + x^2 - 5x`. Use numpy for the sin calculation and do not take any other arguments besides `x`.
"""

import numpy as np

def non_linear_eq(x):
    # Define a non-linear equation
    y = np.sin(x) + x**2 - 5*x
    return y