"""
QUESTION:
Identify the characteristics of the 125 largest values in a historical time series of hourly electricity consumption data for a year. The goal is to develop a method to predict critical peak points in real-time based on the next 24 hours of forecasted electricity consumption. The solution should analyze the historical time series data to find patterns or characteristics of the peak values, such as distance from the mean, z-score, and other statistical properties.
"""

import numpy as np
import pandas as pd

def peak_identification(data, threshold=3, num_peaks=125):
    """
    Identifies the characteristics of the peak values in a historical time series data.

    Parameters:
    data (pandas.Series): Historical time series data
    threshold (int, optional): Z-score threshold for peak identification. Defaults to 3.
    num_peaks (int, optional): Number of peak values to identify. Defaults to 125.

    Returns:
    peak_values (pandas.Series): Peak values in the time series data
    """

    # Calculate descriptive statistics
    mean = data.mean()
    std_dev = data.std()
    median = data.median()
    quartiles = data.quantile([0.25, 0.5, 0.75])

    # Calculate Z-scores
    z_scores = (data - mean) / std_dev

    # Identify peak values based on Z-scores
    peak_values = data[z_scores > threshold]

    # Get the top N peak values
    peak_values = peak_values.nlargest(num_peaks)

    return peak_values