"""
QUESTION:
Write a function `remove_spikes` that takes a numpy array `time_series` representing a time series and returns a new numpy array with the spikes removed. A spike is defined as a data point that deviates from the surrounding values by more than 3 times the median absolute deviation from the median of the time series. The function should replace spike values with the median of the time series.
"""

import numpy as np

def remove_spikes(time_series: np.ndarray) -> np.ndarray:
    """
    Removes spikes from the given time series.

    Parameters
    ----------
    time_series : numpy.ndarray
        Your time series.

    Returns
    -------
    numpy.ndarray:
        Numpy array of time series without spikes.
    """
    # Calculate the median of the time series
    median = np.median(time_series)

    # Calculate the median absolute deviation (MAD) of the time series
    mad = np.median(np.abs(time_series - median))

    # Define a threshold for spike detection (e.g., 3 times MAD)
    threshold = 3.0 * mad

    # Identify spikes by comparing the absolute difference with the median
    spikes = np.abs(time_series - median) > threshold

    # Replace spike values with the median of the time series
    cleaned_series = np.where(spikes, median, time_series)

    return cleaned_series