"""
QUESTION:
Create a function `calculate_noise` that measures the noise in time series data. The function should take a list of numbers as input and return a value that quantifies the average change from one data point to the next. The function should be able to handle outliers and provide a measure of the average change that is not heavily affected by large outliers.
"""

import numpy as np

def calculate_noise(time_series):
    """
    Calculate the noise in time series data.
    
    This function calculates the standard deviation of the differences between adjacent points in the time series.
    It provides a measure of the average change from one data point to the next that is not heavily affected by large outliers.
    
    Parameters:
    time_series (list): A list of numbers representing the time series data.
    
    Returns:
    float: The standard deviation of the differences between adjacent points.
    """
    
    # Calculate the differences between adjacent points
    differences = np.diff(time_series)
    
    # Calculate the standard deviation of the differences
    noise = np.std(differences)
    
    return noise

def calculate_noise_mad(time_series):
    """
    Calculate the noise in time series data using the mean absolute deviation.
    
    This function calculates the mean absolute deviation of the differences between adjacent points in the time series.
    It provides a measure of the average change from one data point to the next that is not heavily affected by large outliers.
    
    Parameters:
    time_series (list): A list of numbers representing the time series data.
    
    Returns:
    float: The mean absolute deviation of the differences between adjacent points.
    """
    
    # Calculate the differences between adjacent points
    differences = np.diff(time_series)
    
    # Calculate the mean absolute deviation of the differences
    noise = np.mean(np.abs(differences))
    
    return noise