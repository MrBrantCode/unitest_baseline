"""
QUESTION:
Detect outliers in a normally distributed dataset using the z-score method. 

Write a function named `detect_outliers_z_score` that takes a list of numbers `data` and an optional threshold `threshold` (default 3) as input. The function should calculate the mean and standard deviation of the input data, and then identify the data points with a z-score greater than the threshold. Return the identified outliers.
"""

import numpy as np

def detect_outliers_z_score(data, threshold=3):
    """
    Detect outliers in a normally distributed dataset using the z-score method.

    Args:
        data (list): A list of numbers.
        threshold (int, optional): The z-score threshold. Defaults to 3.

    Returns:
        list: The identified outliers.
    """
    # Calculate the mean and standard deviation of the input data
    mean = np.mean(data)
    std_dev = np.std(data)

    # Identify the data points with a z-score greater than the threshold
    outliers = [x for x in data if abs((x - mean) / std_dev) > threshold]

    return outliers