"""
QUESTION:
Write a function named `update_weights` that takes in `weights`, `learning_rate`, `x`, `y`, `predictions`, `gradients`, and `decay_factor` as inputs, and updates the `weights` using Stochastic Gradient Descent (SGD) with a learning rate that decays every 10 epochs.
"""

def update_weights(weights, learning_rate, x, y, predictions, gradients, decay_factor):
    for i in range(len(weights)):
        weights[i] -= learning_rate * gradients[i]
    return weights