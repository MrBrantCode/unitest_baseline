"""
QUESTION:
Write a Python function `calculate_variance_covariance_matrix` that takes a 2D array `data` with dimensions (n, p) as input, where n is the number of observations and p is the number of variables, and returns the variance-covariance matrix for the variables in the data.
"""

import numpy as np

def calculate_variance_covariance_matrix(data):
    # Center the data by subtracting the mean of each variable
    centered_data = data - np.mean(data, axis=0)
    
    # Calculate the variance-covariance matrix
    variance_covariance_matrix = np.dot(centered_data.T, centered_data) / (data.shape[0] - 1)
    
    return variance_covariance_matrix