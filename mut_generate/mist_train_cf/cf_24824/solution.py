"""
QUESTION:
Create a function to perform simple linear regression on a dataset. The function should take in two parameters: a dependent variable y and an independent variable x. Implement the function in a way that returns the coefficients of the linear regression model.
"""

import numpy as np

def simple_linear_regression(x, y):
    """
    This function performs simple linear regression on a dataset and returns the coefficients.
    
    Parameters:
    x (list or numpy array): Independent variable.
    y (list or numpy array): Dependent variable.
    
    Returns:
    tuple: A tuple containing the slope and intercept of the linear regression model.
    """
    
    # Convert input to numpy arrays
    x = np.array(x)
    y = np.array(y)
    
    # Calculate the mean of x and y
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    
    # Calculate the slope (beta1) and intercept (beta0) of the linear regression model
    numerator = np.sum((x - mean_x) * (y - mean_y))
    denominator = np.sum((x - mean_x) ** 2)
    beta1 = numerator / denominator
    beta0 = mean_y - beta1 * mean_x
    
    return beta1, beta0