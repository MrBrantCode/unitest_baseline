"""
QUESTION:
Write a function `calculate_mean_std` that takes the means and standard deviations of two independent random variables X and Y as input, and returns the mean and standard deviation of the sum of these variables (X+Y). The function should accept four parameters: `mu_X`, `mu_Y`, `sigma_X`, and `sigma_Y`, representing the mean of X, mean of Y, standard deviation of X, and standard deviation of Y, respectively. The function should return a tuple containing the mean and standard deviation of X+Y.
"""

import numpy as np

def calculate_mean_std(mu_X, mu_Y, sigma_X, sigma_Y):
    """
    Calculate the mean and standard deviation of the sum of two independent random variables X and Y.

    Parameters:
    mu_X (float): Mean of X
    mu_Y (float): Mean of Y
    sigma_X (float): Standard deviation of X
    sigma_Y (float): Standard deviation of Y

    Returns:
    tuple: A tuple containing the mean and standard deviation of X+Y
    """
    # Calculate the mean of X + Y
    mu_XY = mu_X + mu_Y

    # Calculate the standard deviation of X + Y
    sigma_XY = np.sqrt(sigma_X**2 + sigma_Y**2)

    return mu_XY, sigma_XY