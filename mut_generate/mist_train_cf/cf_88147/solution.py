"""
QUESTION:
Write a function called `calculate_mean_and_median` that takes a list of numbers as input and returns the mean and median of the data set while excluding any values that are more than 3 standard deviations away from the mean. Outliers should be replaced with the mean value of the remaining data set.
"""

import numpy as np

def calculate_mean_and_median(data):
    mean = np.mean(data)
    std_dev = np.std(data)
    threshold = 3 * std_dev

    data_no_outliers = [mean if abs(x - mean) > threshold else x for x in data]
    
    mean_no_outliers = np.mean(data_no_outliers)
    median_no_outliers = np.median(data_no_outliers)
    
    return mean_no_outliers, median_no_outliers