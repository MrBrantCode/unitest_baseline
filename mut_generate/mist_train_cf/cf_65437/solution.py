"""
QUESTION:
Create a function that calculates the Residual Sum of Squares (RSS) for linear regression. The function should take in two parameters, Y and Xβ, where Y is the vector of actual values and Xβ is the vector of estimated values. The function should return the RSS value as a scalar. Ensure the function correctly handles the mathematical operation to produce a scalar output.
"""

import numpy as np

def calculate_rss(Y, Xβ):
    """
    This function calculates the Residual Sum of Squares (RSS) for linear regression.
    
    Parameters:
    Y (numpy array): A vector of actual values.
    Xβ (numpy array): A vector of estimated values.
    
    Returns:
    float: The RSS value as a scalar.
    """
    return np.sum((Y - Xβ) ** 2)