"""
QUESTION:
Implement a function `estimate_time_shift(camera_rates, imu_rates)` that takes two arrays of angular rates from cameras and IMU respectively and returns the estimated time shift between the two data sources. The time shift is calculated using the cross-correlation between the two arrays, where the maximum correlation value corresponds to the time shift. The function assumes that the biases are small and the angular rates are constant on a fixed body independent of location.

The function should take in two parameters: `camera_rates` and `imu_rates`, both of which are lists of floats representing the angular rates from the cameras and the IMU respectively. The function should return an integer representing the estimated time shift.
"""

from typing import List
import numpy as np

def estimate_time_shift(camera_rates: List[float], imu_rates: List[float]) -> int:
    # Calculate the cross-correlation between camera and imu rates
    cross_corr = np.correlate(camera_rates, imu_rates, mode='full')
    
    # Find the index of the maximum correlation value
    max_corr_index = np.argmax(cross_corr)
    
    # Calculate the time shift as the difference between the lengths of the input arrays and the index of maximum correlation
    time_shift = len(camera_rates) - max_corr_index
    
    return time_shift