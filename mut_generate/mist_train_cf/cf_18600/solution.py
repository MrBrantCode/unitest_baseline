"""
QUESTION:
Create a function `calculate_filtered_mean_and_median` that takes a list of numbers as input. The function should calculate and return the mean and median of the input list, excluding any numbers that are more than 2 standard deviations away from the mean.
"""

import numpy as np
import statistics

def calculate_filtered_mean_and_median(data):
    """
    Calculate the mean and median of a list of numbers, excluding any numbers that are more than 2 standard deviations away from the mean.

    Args:
        data (list): A list of numbers.

    Returns:
        tuple: A tuple containing the filtered mean and median.
    """

    # Calculate the mean and standard deviation of the dataset
    mean = np.mean(data)
    std_dev = np.std(data)

    # Define the threshold for outliers based on the 2 standard deviations away from the mean
    threshold = 2 * std_dev

    # Create a new dataset excluding the outliers
    filtered_data = [x for x in data if (mean - threshold) <= x <= (mean + threshold)]

    # Calculate the mean and median of the filtered dataset
    filtered_mean = np.mean(filtered_data)
    filtered_median = statistics.median(filtered_data)

    return filtered_mean, filtered_median