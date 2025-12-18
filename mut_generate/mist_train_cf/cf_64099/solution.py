"""
QUESTION:
Write a function called `average_lag_correlation` that calculates the average time lag at which two time-series measurements are most strongly correlated across multiple people. The function should take in a dictionary `data` where each key represents a person and the corresponding value is another dictionary with two time-series measurements. The function should return the average time lag. 

The function should use time-lagged cross-correlation analysis for each person and then average over the lags identified for each individual. Assume that the time-series measurements for each person have the same length.
"""

import numpy as np

def average_lag_correlation(data, measurement1, measurement2):
    """
    Calculate the average time lag at which two time-series measurements are most strongly correlated across multiple people.

    Args:
        data (dict): A dictionary where each key represents a person and the corresponding value is another dictionary with two time-series measurements.
        measurement1 (str): The key for the first time-series measurement.
        measurement2 (str): The key for the second time-series measurement.

    Returns:
        float: The average time lag.
    """
    lag_correlation = []
    for person in data.values():
        ts1 = person[measurement1]
        ts2 = person[measurement2]
        correlation = np.correlate(ts1, ts2, mode='full')
        max_corr = max(correlation)
        lag_at_max = correlation.tolist().index(max_corr)
        lag_correlation.append(lag_at_max)
    average_lag = sum(lag_correlation)/len(lag_correlation)
    return average_lag