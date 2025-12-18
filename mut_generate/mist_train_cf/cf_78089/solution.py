"""
QUESTION:
Write a function `calculate_delta` that calculates the error delta for a neuron in a neural network layer. The function should take the error delta of the next layer, the weights of the next layer, and the derivative of the activation function of the current layer as inputs and returns the calculated error delta. The function should use the formula derived from the chain rule for backpropagation: `delta^k = (W^(k+1))^T * delta^(k+1) .* sigma'(z^(k))`. The function should support element-wise multiplication and should return the result of this operation.
"""

import numpy as np

def calculate_delta(next_layer_delta, next_layer_weights, derivative):
    """
    Calculate the error delta for a neuron in a neural network layer.
    
    Parameters:
    next_layer_delta (numpy array): Error delta of the next layer.
    next_layer_weights (numpy array): Weights of the next layer.
    derivative (numpy array): Derivative of the activation function of the current layer.
    
    Returns:
    numpy array: Calculated error delta.
    """
    return np.dot(next_layer_weights.T, next_layer_delta) * derivative