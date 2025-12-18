"""
QUESTION:
Write a function `convergence_criterion` that takes in two arrays of parameter estimates (`beta_old` and `beta_new`) and a small value (`epsilon`) as inputs, and returns `True` if the relative change between `beta_old` and `beta_new` is smaller than `epsilon`, and `False` otherwise. The relative change is calculated as the Euclidean norm of the difference between `beta_new` and `beta_old`, divided by the Euclidean norm of `beta_old`.
"""

import numpy as np

def convergence_criterion(beta_old, beta_new, epsilon):
    """
    Check if the relative change between beta_old and beta_new is smaller than epsilon.

    Args:
        beta_old (numpy array): Old parameter estimates.
        beta_new (numpy array): New parameter estimates.
        epsilon (float): Small value.

    Returns:
        bool: True if the relative change is smaller than epsilon, False otherwise.
    """

    # Calculate the Euclidean norm of the difference between beta_new and beta_old
    diff_norm = np.linalg.norm(beta_new - beta_old)
    
    # Calculate the Euclidean norm of beta_old
    old_norm = np.linalg.norm(beta_old)
    
    # Check if the relative change is smaller than epsilon
    # Avoid division by zero by adding a small value to old_norm
    return diff_norm / (old_norm + 1e-9) < epsilon