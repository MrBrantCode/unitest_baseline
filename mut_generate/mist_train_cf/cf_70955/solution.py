"""
QUESTION:
Compute the multi-category logarithmic loss (or cross-entropy loss) of a decision tree's output. The function should take two parameters: `actual_classes` and `forecasted_probabilities`, where `actual_classes` is a list of true class labels (1-indexed) and `forecasted_probabilities` is a 2D list of predicted probabilities for each class. The function should return the average logarithmic loss.
"""

import numpy as np

def multi_category_logloss(actual_classes, forecasted_probabilities):
    """
    Compute the multi-category logarithmic loss (or cross-entropy loss).

    Parameters:
    actual_classes (list): A list of true class labels (1-indexed).
    forecasted_probabilities (2D list): A 2D list of predicted probabilities for each class.

    Returns:
    float: The average logarithmic loss.
    """
    actual_classes = np.array(actual_classes) - 1  # subtract 1 because Python uses 0-based indexing
    forecasted_probabilities = np.array(forecasted_probabilities)
    
    # One-hot encode the actual classes
    n_samples = len(actual_classes)
    n_categories = len(forecasted_probabilities[0])
    actual_classes_one_hot = np.zeros((n_samples, n_categories))
    actual_classes_one_hot[np.arange(n_samples), actual_classes] = 1

    # Compute the multi-category logarithmic loss
    logloss = -np.sum(np.log(forecasted_probabilities) * actual_classes_one_hot) / n_samples
    return logloss