"""
QUESTION:
Write a function `calculate_filtered_mean_and_median` that takes a list of numbers as input, calculates the mean and median of the list while excluding any outliers that are 2 standard deviations away from the mean, and returns the filtered mean and median. The function should use numpy for efficient numerical computations.
"""

import numpy as np
import statistics

def calculate_filtered_mean_and_median(data):
    mean = np.mean(data)
    std_dev = np.std(data)
    threshold = 2 * std_dev
    filtered_data = [x for x in data if (mean - threshold) <= x <= (mean + threshold)]
    filtered_mean = np.mean(filtered_data)
    filtered_median = statistics.median(filtered_data)
    return filtered_mean, filtered_median