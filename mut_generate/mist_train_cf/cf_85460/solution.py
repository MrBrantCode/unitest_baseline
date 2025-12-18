"""
QUESTION:
Write a Python function, `calculate_error`, to implement the given mathematical equation δ^l_j = ∑_k (w^l+1_kj δ^l+1_k) σ′(z^l_j) which represents the error of the j-th neuron in the l-th layer of a neural network, where the error of each neuron is dependent on the error of the next layer and the weights connecting them. The function should take as input the weights `w`, the error of the next layer `delta_next`, and the derivative of the activation function `activation_derivative`.
"""

import numpy as np

def calculate_error(w, delta_next, activation_derivative):
    """
    Calculate the error of the j-th neuron in the l-th layer of a neural network.

    Parameters:
    w (numpy array): Weights linking the current layer to the next layer.
    delta_next (numpy array): Errors of the neurons in the next layer.
    activation_derivative (numpy array): Derivative of the activation function evaluated at the current layer.

    Returns:
    numpy array: Error of the current layer.
    """
    # Calculate the weighted sum of the errors of the next layer
    weighted_errors = np.dot(w, delta_next)
    
    # Calculate the error of the current layer by multiplying the weighted sum with the derivative of the activation function
    error = weighted_errors * activation_derivative
    
    return error