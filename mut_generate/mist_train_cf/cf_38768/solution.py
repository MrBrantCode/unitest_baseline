"""
QUESTION:
Implement a function `forward_propagation` that takes input data `X` and model parameters `W1`, `b1`, `W2`, and `b2` and returns the output of a neural network after forward propagation. The function should use the hyperbolic tangent activation function for the first layer. The input data `X` and the model parameters should be numpy arrays. The function should return a numpy array representing the output of the neural network. 

Function signature: `def forward_propagation(X, W1, b1, W2, b2) -> np.ndarray:`
"""

import numpy as np

def forward_propagation(X, W1, b1, W2, b2) -> np.ndarray:
    z1 = X.dot(W1) + b1
    a1 = np.tanh(z1)
    output = a1.dot(W2) + b2
    return output