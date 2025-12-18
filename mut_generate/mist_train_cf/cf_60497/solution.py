"""
QUESTION:
Write a Python function, `r_squared_loss_function`, to train a model using R-squared (coefficient of determination) as the loss function. Consider the caveats of using R-squared, including sensitivity to outliers, non-convexity, and interpretation.
"""

import numpy as np

def r_squared_loss_function(y_true, y_pred):
    """
    R-squared (coefficient of determination) loss function.
    
    Parameters:
    y_true (array-like): Ground truth target values.
    y_pred (array-like): Estimated targets as returned by a regression model.
    
    Returns:
    float: R-squared value.
    """
    
    # Calculate the mean of the true values
    mean_y_true = np.mean(y_true)
    
    # Calculate the total sum of squares
    ss_tot = np.sum((y_true - mean_y_true) ** 2)
    
    # Calculate the residual sum of squares
    ss_res = np.sum((y_true - y_pred) ** 2)
    
    # Calculate the R-squared value
    r_squared = 1 - (ss_res / ss_tot)
    
    return r_squared