"""
QUESTION:
What is the range of outputs for the ReLU (Rectified Linear Unit) activation function in a neural network? The function should return a value based on the input, where for any negative input, it returns 0, and for any positive input, it returns the input value.
"""

def ReLU(x):
    """
    Rectified Linear Unit activation function.

    Args:
        x (float): Input value.

    Returns:
        float: Output value.
    """
    return max(0, x)