"""
QUESTION:
Implement a function `lead_lag_estimation(ts1, ts2)` that takes two NumPy arrays `ts1` and `ts2` as input and returns the lead or lag value as an integer representing the time delay between the two time series. The function should have a time complexity of O(n log n) and handle time series of varying lengths. If the returned value is positive, it indicates that `ts1` leads `ts2` by that many time steps, and if it is negative, it indicates that `ts2` leads `ts1` by that many time steps.
"""

import numpy as np

def lead_lag_estimation(ts1: np.ndarray, ts2: np.ndarray) -> int:
    cross_corr = np.correlate(ts1, ts2, mode='full')
    lead_lag = np.argmax(cross_corr) - (len(ts1) - 1)
    return lead_lag