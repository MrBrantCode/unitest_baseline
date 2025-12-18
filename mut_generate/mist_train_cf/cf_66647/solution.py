"""
QUESTION:
Calculate the statistical properties of a given dataset. 

Write a function called `calculate_statistics` that takes an array of numbers as input and returns a dictionary with the keys 'range', 'interquartile_range', and 'standard_deviation' containing the corresponding values. The function should calculate the range, interquartile range, and standard deviation of the input data.
"""

import numpy as np
import statistics

def calculate_statistics(data):
    """
    Calculate the statistical properties of a given dataset.

    Args:
    data (list): A list of numbers.

    Returns:
    dict: A dictionary with the keys 'range', 'interquartile_range', and 'standard_deviation' containing the corresponding values.
    """
    
    data_range = np.ptp(data)
    q75, q25 = np.percentile(data, [75 ,25])
    iqr = q75 - q25
    std_dev = statistics.stdev(data)
    
    return {
        'range': data_range,
        'interquartile_range': iqr,
        'standard_deviation': std_dev
    }