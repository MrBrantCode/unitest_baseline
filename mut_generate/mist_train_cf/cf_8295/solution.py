"""
QUESTION:
Write a recursive function named `linear_regression` that calculates the linear regression line for a given dataset. The function should take two parameters: `x` and `y`, which are lists of numbers representing the input and output values of the dataset, respectively.
"""

import numpy as np

def linear_regression(x, y):
    """
    This function calculates the linear regression line for a given dataset.
    
    Parameters:
    x (list): A list of numbers representing the input values of the dataset.
    y (list): A list of numbers representing the output values of the dataset.
    
    Returns:
    tuple: A tuple containing the slope and intercept of the linear regression line.
    """
    x = np.array(x)
    y = np.array(y)
    n = len(x)
    
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    
    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sum((x - x_mean) ** 2)
    
    m = numerator / denominator
    b = y_mean - m * x_mean
    
    return m, b