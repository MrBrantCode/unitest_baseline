"""
QUESTION:
Write a function named `estimate_population_quantile` to calculate the average of sample quantiles and estimate the true population quantile. The function should take two parameters: `samples` (a 2D array containing N samples of 100 numbers each, all drawn IID from the same distribution) and `quantile` (a float representing the desired quantile, e.g., 0.95 for the 95th quantile). The function should return the estimated population quantile as a float.
"""

import numpy as np

def estimate_population_quantile(samples, quantile):
    """
    Calculate the average of sample quantiles to estimate the true population quantile.

    Parameters:
    samples (2D array): A 2D array containing N samples of 100 numbers each, 
                        all drawn IID from the same distribution.
    quantile (float): A float representing the desired quantile, 
                      e.g., 0.95 for the 95th quantile.

    Returns:
    float: The estimated population quantile.
    """
    # Calculate the quantile for each sample
    sample_quantiles = np.quantile(samples, quantile, axis=1)
    
    # Calculate the average of the sample quantiles
    estimated_population_quantile = np.mean(sample_quantiles)
    
    return estimated_population_quantile