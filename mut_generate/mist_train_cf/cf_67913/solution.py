"""
QUESTION:
Design a function named binary_cross_entropy_loss that calculates the cross-entropy loss for a binary classification task. The function should take as input a true class label y and a predicted probability p. The function should output the cross-entropy loss. The function should be applicable to a set of N instances where for each instance n, y_n is either 0 (negative class) or 1 (positive class), and p_n is the estimated probability of it belonging to the positive class.
"""

import numpy as np

def binary_cross_entropy_loss(y, p):
    """
    Calculate the cross-entropy loss for a binary classification task.

    Parameters:
    y (numpy array): True class labels (0 or 1)
    p (numpy array): Predicted probabilities of the positive class

    Returns:
    float: Cross-entropy loss
    """
    # Ensure inputs are numpy arrays
    y = np.array(y)
    p = np.array(p)

    # Clip predicted probabilities to avoid division by zero
    epsilon = 1e-15
    p = np.clip(p, epsilon, 1 - epsilon)

    # Calculate cross-entropy loss
    loss = -np.mean(y * np.log(p) + (1 - y) * np.log(1 - p))

    return loss