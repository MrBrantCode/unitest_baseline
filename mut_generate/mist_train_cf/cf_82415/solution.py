"""
QUESTION:
Write a function `ols_residuals_regression` to demonstrate the property of OLS regressions where the estimated residuals are uncorrelated with the explanatory variables, resulting in the OLS estimator $\hat{\gamma}$ being a vector of zeros. The function should take a 2D array `X` of explanatory variables and a 1D array `y` of response variables as input. The function should not take any other parameters.
"""

import numpy as np

def ols_residuals_regression(X, y):
    """
    This function demonstrates the property of OLS regressions where the estimated residuals 
    are uncorrelated with the explanatory variables, resulting in the OLS estimator γ being 
    a vector of zeros.

    Parameters:
    X (2D array): A 2D array of explanatory variables.
    y (1D array): A 1D array of response variables.

    Returns:
    None
    """

    # Calculate the coefficients using the normal equation
    coefficients = np.linalg.inv(X.T @ X) @ X.T @ y
    
    # Predict the response variable using the coefficients
    predicted_y = X @ coefficients
    
    # Calculate the residuals
    residuals = y - predicted_y
    
    # Regress the residuals on X
    gamma = np.linalg.inv(X.T @ X) @ X.T @ residuals
    
    # Return gamma
    return gamma