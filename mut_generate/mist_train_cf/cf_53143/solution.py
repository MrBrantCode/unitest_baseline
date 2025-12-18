"""
QUESTION:
Write a function called `calculate_union_correlation` that calculates the Pearson correlation coefficient for the union of two sets of 2D points, A and B. The function should take as input the Pearson correlation coefficients of A and B, as well as their respective means, variances, and sizes.
"""

import numpy as np

def calculate_union_correlation(r_A, r_B, mean_A, mean_B, var_A, var_B, size_A, size_B, x_A, x_B):
    """
    Calculate the Pearson correlation coefficient for the union of two sets of 2D points, A and B.

    Args:
        r_A (float): The Pearson correlation coefficient of set A.
        r_B (float): The Pearson correlation coefficient of set B.
        mean_A (list): The mean of set A.
        mean_B (list): The mean of set B.
        var_A (list): The variance of set A.
        var_B (list): The variance of set B.
        size_A (int): The size of set A.
        size_B (int): The size of set B.
        x_A (list): Set A.
        x_B (list): Set B.

    Returns:
        float: The Pearson correlation coefficient for the union of sets A and B.
    """
    
    # Combine the two datasets
    x = np.concatenate((x_A, x_B))
    
    # Calculate the mean and variance of the combined dataset
    mean = np.mean(x, axis=0)
    var = np.var(x, axis=0)
    
    # Calculate the covariance between the two variables in the combined dataset
    cov = np.mean((x[:, 0] - mean[0]) * (x[:, 1] - mean[1]))
    
    # Calculate the Pearson correlation coefficient for the combined dataset
    r = cov / np.sqrt(var[0] * var[1])
    
    return r