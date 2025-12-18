"""
QUESTION:
Given two square-integrable random variables X and Y with the same moments (i.e., EX^n = EY^n for all non-negative integers n), prove that X and Y have the same distribution (and thus the same PDF, if it exists) using their characteristic functions CX(t) and CY(t). The solution should be based on the uniqueness property of the characteristic function and the fact that it encodes all the moments of the distribution.
"""

import numpy as np

def same_distribution(moments_X, moments_Y):
    """
    This function checks if two random variables X and Y have the same distribution 
    based on the uniqueness property of their characteristic functions and the fact 
    that it encodes all the moments of the distribution.

    Parameters:
    moments_X (list): A list of moments of random variable X.
    moments_Y (list): A list of moments of random variable Y.

    Returns:
    bool: True if X and Y have the same distribution, False otherwise.
    """

    # Check if the moments of X and Y are the same
    if np.array_equal(moments_X, moments_Y):
        # If the moments are the same, then X and Y have the same distribution
        return True
    else:
        # If the moments are not the same, then X and Y do not have the same distribution
        return False