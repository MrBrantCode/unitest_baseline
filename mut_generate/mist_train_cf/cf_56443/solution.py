"""
QUESTION:
Implement a function named `stationarize_time_series` to transform a given non-stationary time series dataset into a stationary one, addressing issues such as changing mean, changing variance, trends, seasonality, and instability that affect cluster formation during data analysis. The function should take a 1D numpy array representing the time series data as input and return the transformed stationary time series data.
"""

import numpy as np

def stationarize_time_series(time_series_data):
    """
    This function transforms a given non-stationary time series dataset into a stationary one.

    Parameters:
    time_series_data (numpy array): A 1D numpy array representing the time series data.

    Returns:
    numpy array: The transformed stationary time series data.
    """
    
    # Calculate the first difference of the time series
    first_diff = np.diff(time_series_data)
    
    # Return the first difference as the stationarized time series
    return first_diff