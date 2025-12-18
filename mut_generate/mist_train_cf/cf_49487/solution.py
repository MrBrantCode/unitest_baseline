"""
QUESTION:
Implement a function named `calculate_error_estimation` that takes in parameters `num_samples`, `num_features`, and `sampling_ratio` to estimate the error made by sampling data instead of using the entire dataset, as described in Theorem 3.2 of the LightGBM paper. The function should not take any additional parameters.
"""

import math

def calculate_error_estimation(num_samples, num_features, sampling_ratio):
    """
    This function estimates the error made by sampling data instead of using the entire dataset,
    as described in Theorem 3.2 of the LightGBM paper.

    Parameters:
    num_samples (int): The total number of samples.
    num_features (int): The total number of features.
    sampling_ratio (float): The ratio of samples to be taken.

    Returns:
    float: The estimated error.
    """
    return math.sqrt((1 + (num_features - 1) / (2 * num_samples)) / (2 * sampling_ratio))