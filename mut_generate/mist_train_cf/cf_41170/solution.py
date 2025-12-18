"""
QUESTION:
Write a Python function `calculate_mean_sic` that takes a 3D NumPy array `sicmo` representing sea ice concentration values over time and space, a 1D NumPy array `years` containing the corresponding years for the time dimension, and two integers `start_year` and `end_year` representing the start and end years of the time period. The function should calculate the mean sea ice concentration over the specified time period and return the result as a 2D NumPy array, where each element represents the mean sea ice concentration at a specific latitude and longitude, presented as a percentage.
"""

import numpy as np

def calculate_mean_sic(sicmo, years, start_year, end_year):
    yearq = np.where((years >= start_year) & (years <= end_year))[0]
    mean_sic = np.nanmean(sicmo[yearq, :, :], axis=0) * 100
    return mean_sic