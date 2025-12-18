"""
QUESTION:
Write a function `cross_entropy_loss` that calculates the cross-entropy loss for a binary classification model. The function should take two parameters: `y_true` (a list of true labels, either 0 or 1) and `y_pred` (a list of predicted probabilities). The function should return the cross-entropy loss as a single value. The loss function should be calculated as -1/N * (sum of (y_n * log(p_n) + (1-y_n) * log(1-p_n)) for all n), where N is the number of samples, y_n is the true label, and p_n is the predicted probability.
"""

import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Calculate the cross-entropy loss for a binary classification model.

    Parameters:
    y_true (list): A list of true labels, either 0 or 1.
    y_pred (list): A list of predicted probabilities.

    Returns:
    float: The cross-entropy loss.
    """
    
    # Ensure inputs are numpy arrays
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    
    # Clip predicted probabilities to avoid division by zero
    epsilon = 1e-15
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    
    # Calculate cross-entropy loss
    loss = -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
    
    return loss