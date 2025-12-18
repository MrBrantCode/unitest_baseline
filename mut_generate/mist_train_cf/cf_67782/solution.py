"""
QUESTION:
Write a function `relu_derivative` that takes one argument `x` and returns the derivative of the Rectified Linear Unit (ReLU) function for the given `x`. The ReLU function is defined as `max(0, x)`, and its derivative is 1 for `x > 0` and 0 for `x < 0`. 

Also, write a function `sigmoid_derivative` that takes one argument `x` and returns the derivative of the sigmoid function for the given `x`. The sigmoid function is defined as `1 / (1 + e^(-x))`, and its derivative is `σ(x) * (1 - σ(x))`.
"""

def relu_derivative(x):
    """
    Returns the derivative of the Rectified Linear Unit (ReLU) function for the given x.
    
    :param x: The input value.
    :return: The derivative of the ReLU function.
    """
    return 1 if x > 0 else 0


def sigmoid_derivative(x):
    """
    Returns the derivative of the sigmoid function for the given x.
    
    :param x: The input value.
    :return: The derivative of the sigmoid function.
    """
    sigmoid = 1 / (1 + 2.71828 ** -x)
    return sigmoid * (1 - sigmoid)