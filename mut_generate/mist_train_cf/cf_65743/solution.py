"""
QUESTION:
Write a function named `calculate_correlation` that calculates the correlation between a variable of percent change return and a variable of dollar change or basis points, considering whether standardization is required for accurate calculation. The function should use Pearson's correlation coefficient formula and be implemented in Python.
"""

import numpy as np

def calculate_correlation(x, y):
    """
    Calculate the correlation between two variables using Pearson's correlation coefficient.
    
    Args:
        x (list or numpy array): The first variable.
        y (list or numpy array): The second variable.
    
    Returns:
        float: The Pearson correlation coefficient.
    """
    return np.corrcoef(x, y)[0, 1]