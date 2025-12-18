"""
QUESTION:
Write a function named `bayesian_ab_testing` that calculates the 95% Highest Density Interval (HDI) from a given posterior distribution. The function should return the lower and upper bounds of the 95% HDI. The HDI is defined as the shortest interval that contains 95% of the posterior distribution, which in this case should be between the 2.5th percentile and the 97.5th percentile of the posterior distribution.
"""

import numpy as np

def bayesian_ab_testing(posterior_distribution):
    """
    Calculate the 95% Highest Density Interval (HDI) from a given posterior distribution.

    Args:
    posterior_distribution (numpy array): The posterior distribution.

    Returns:
    tuple: A tuple containing the lower and upper bounds of the 95% HDI.
    """
    lower_bound = np.percentile(posterior_distribution, 2.5)
    upper_bound = np.percentile(posterior_distribution, 97.5)
    return lower_bound, upper_bound