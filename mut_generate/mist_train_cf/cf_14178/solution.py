"""
QUESTION:
Calculate the weighted standard deviation of a set of data points with corresponding weights.

Given two lists of equal length, `data_points` and `weights`, write a function `weighted_standard_deviation` that returns the weighted standard deviation of the data points. The weights should be non-negative and not all zero. The function should be able to handle lists of floating point numbers.
"""

import math

def weighted_standard_deviation(data_points, weights):
    # Calculate the weighted mean
    weighted_mean = sum(data * weight for data, weight in zip(data_points, weights)) / sum(weights)
    
    # Calculate the squared differences from the weighted mean
    squared_diff = [(data - weighted_mean) ** 2 for data in data_points]
    
    # Calculate the weighted sum of squared differences
    weighted_sum = sum(weight * squared for weight, squared in zip(weights, squared_diff))
    
    # Calculate the weighted variance
    weighted_variance = weighted_sum / sum(weights)
    
    # Calculate the weighted standard deviation
    weighted_std_dev = math.sqrt(weighted_variance)
    
    return weighted_std_dev