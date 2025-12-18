"""
QUESTION:
Write a function `compare_residuals` that takes the predicted values and actual values as input, and calculates the residuals for L1 and L2 error metrics. Assume the residuals can be used to predict the efficacy of a model on a validation set. 

Restrictions: The function should take two lists of numbers (predicted and actual values) as input and return a tuple of two numbers representing the L1 and L2 residuals.
"""

import numpy as np

def compare_residuals(predicted, actual):
    """
    Calculate L1 and L2 residuals from predicted and actual values.

    Args:
    predicted (list): List of predicted values.
    actual (list): List of actual values.

    Returns:
    tuple: A tuple containing L1 and L2 residuals.
    """
    # Ensure inputs are numpy arrays
    predicted = np.array(predicted)
    actual = np.array(actual)

    # Calculate residuals
    residuals = predicted - actual

    # Calculate L1 residual
    l1_residual = np.sum(np.abs(residuals))

    # Calculate L2 residual
    l2_residual = np.sqrt(np.sum(residuals ** 2))

    return l1_residual, l2_residual