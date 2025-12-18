"""
QUESTION:
Write a function `calculate_accuracy(X, W1, B1, W2, B2, Y)` that takes the input data `X`, weights `W1` and `W2`, biases `B1` and `B2`, and the true labels `Y`, and returns the accuracy of the predictions. The function should first predict the output using the given weights, biases, and input data, and then calculate the accuracy by comparing the predicted output with the true labels. The predicted output should be a binary classification result (0 or 1), and the accuracy should be the proportion of correctly classified examples.
"""

import numpy as np

def calculate_accuracy(X, W1, B1, W2, B2, Y):
    """
    Calculates the accuracy of the predictions.

    Args:
    X: NumPy array of shape (n, m), where n is the number of features and m is the number of examples.
    W1: NumPy array of shape (n_h, n), where n_h is the number of hidden units and n is the number of features.
    B1: NumPy array of shape (n_h, 1), where n_h is the number of hidden units.
    W2: NumPy array of shape (1, n_h), where n_h is the number of hidden units.
    B2: NumPy array of shape (1, 1).
    Y: NumPy array of true labels of shape (m, ).

    Returns:
    Accuracy of the predictions.
    """
    Z1 = np.dot(W1, X) + B1
    A1 = np.tanh(Z1)
    Z2 = np.dot(W2, A1) + B2
    A2 = 1 / (1 + np.exp(-Z2))
    Y_predicted = (A2 > 0.5).astype(int)
    accuracy = np.mean(Y_predicted == Y)

    return accuracy