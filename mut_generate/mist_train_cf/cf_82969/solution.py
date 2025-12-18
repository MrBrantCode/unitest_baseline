"""
QUESTION:
Write a Python function named `logistic_function` that takes in two parameters `B0` and `B1` and one input `x` and returns the output of the logistic function. The function should not take any other parameters.
"""

import math

def logistic_function(B0, B1, x):
    """
    This function calculates the output of the logistic function.

    Parameters:
    B0 (float): The intercept of the logistic function.
    B1 (float): The slope of the logistic function.
    x (float): The input value.

    Returns:
    float: The output of the logistic function.
    """
    return 1 / (1 + math.exp(-(B0 + B1 * x)))