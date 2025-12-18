"""
QUESTION:
Implement the `softmax` and `softmax_derivative` functions as methods of the `NeuralNetworkActivation` class. The `softmax` function should take a vector `x` as input, clip the values to a range of -700 to 700 for numerical stability, and return the normalized softmax output. The `softmax_derivative` function should compute the derivative of the softmax function using the softmax output. Use the numpy library to handle numerical computations.
"""

import numpy as np

def softmax(x):
    """
    Computes the softmax of a vector.

    Args:
    x (numpy array): Input vector.

    Returns:
    softmax_output (numpy array): Normalized softmax output.
    """
    x = np.clip(x, -700, 700)  # Clip input values for numerical stability
    exp_x = np.exp(x)
    exp_sum = np.sum(exp_x)
    return exp_x / exp_sum

def softmax_derivative(x):
    """
    Computes the derivative of the softmax function.

    Args:
    x (numpy array): Input vector.

    Returns:
    derivative (numpy array): Derivative of the softmax function.
    """
    s = softmax(x)
    return s * (1 - s)