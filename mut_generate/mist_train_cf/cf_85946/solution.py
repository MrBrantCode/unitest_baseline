"""
QUESTION:
Compute the new weights for a single iteration of a perceptron with a sigmoid activation function, given the inputs, expected output, and current weights. The sigmoid function is represented by the equation 1 / (1 + exp(-z)), and the update function for the weights is ∆w = η * e * y_pred * (1 - y_pred) * x, with a learning rate of η=1. The current weights are w1 and w2, and the inputs are x1 and x2.
"""

import math

def update_weights(x1, x2, y, w1, w2):
    z = w1 * x1 + w2 * x2
    y_pred = 1 / (1 + math.exp(-z))
    e = y - y_pred
    dw1 = e * y_pred * (1 - y_pred) * x1
    dw2 = e * y_pred * (1 - y_pred) * x2
    return w1 + dw1, w2 + dw2