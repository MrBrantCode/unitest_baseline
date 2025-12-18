"""
QUESTION:
Write a Python function named `sigmoid` that takes a single real number as input and returns the output of the Sigmoid function for the given input, where the output is restricted to a specific interval. Ensure the output is within the range (0,1).
"""

import math

def sigmoid(x):
    """
    Computes the Sigmoid function for a given input x.

    Args:
    x (float): Input to the Sigmoid function.

    Returns:
    float: Output of the Sigmoid function, restricted to the interval (0,1).
    """
    return 1 / (1 + math.exp(-x))