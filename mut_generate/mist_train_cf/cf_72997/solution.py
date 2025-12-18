"""
QUESTION:
Implement a function named `relu_and_sigmoid_derivatives` that calculates and returns the derivatives of ReLU and Sigmoid functions given an input `x`. The ReLU derivative should be 0 for `x < 0` and 1 for `x > 0`, and the Sigmoid derivative should be `f(x)*(1 - f(x))`. The Sigmoid function is defined as `f(x) = 1 / (1 + e^(-x))`. Note that the function should handle the discontinuity of the ReLU derivative at `x = 0` by setting it to 0 by convention.
"""

import numpy as np

def relu_and_sigmoid_derivatives(x):
    """
    This function calculates and returns the derivatives of ReLU and Sigmoid functions given an input x.

    Parameters:
    x (float): The input value.

    Returns:
    tuple: A tuple containing the derivative of the ReLU function and the derivative of the Sigmoid function.
    """

    # Calculate the derivative of the ReLU function
    # By convention, we set the derivative to 0 at x = 0
    relu_derivative = np.where(x < 0, 0, 1)

    # Calculate the Sigmoid function
    sigmoid = 1 / (1 + np.exp(-x))

    # Calculate the derivative of the Sigmoid function
    sigmoid_derivative = sigmoid * (1 - sigmoid)

    return relu_derivative, sigmoid_derivative