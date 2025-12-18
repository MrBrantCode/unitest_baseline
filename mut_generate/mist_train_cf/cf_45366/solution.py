"""
QUESTION:
Write a function named `calculate_cross_entropy_loss` that calculates the cross-entropy loss between the actual labels and the predicted probabilities. The actual labels should be one-hot encoded, and the function should handle a list of predicted probabilities for multiple samples.

The function should take two parameters: `y_actual` (a list of actual labels) and `y_pred` (a 2D array of predicted probabilities), and return the calculated cross-entropy loss.

Note: The actual labels are 1-indexed, meaning the first class is labeled as 1, the second class as 2, and so on.
"""

import numpy as np

def calculate_cross_entropy_loss(y_actual, y_pred):
    """
    Calculate the cross-entropy loss between the actual labels and the predicted probabilities.

    Parameters:
    y_actual (list): A list of actual labels (1-indexed).
    y_pred (2D array): A 2D array of predicted probabilities.

    Returns:
    float: The calculated cross-entropy loss.
    """
    
    # One-hot encoding of actual labels
    y_actual_encoded = np.zeros(y_pred.shape)
    for i, label in enumerate(y_actual):
        y_actual_encoded[i][label - 1] = 1
    
    # Compute the cross-entropy loss
    cross_entropy_loss = -(y_actual_encoded * np.log(y_pred)).sum()
    
    return cross_entropy_loss