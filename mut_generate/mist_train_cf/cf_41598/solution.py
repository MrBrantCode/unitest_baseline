"""
QUESTION:
Write a function `find_min_distance_time` that takes in two pandas DataFrames `chebyshev_data` and `sqeuclidean_data` and an `eigenstate` name. Each DataFrame contains a 'time' column and columns representing eigenstate data for each state at different time points. The function should calculate the Chebyshev and Euclidean distances for each eigenstate from the initial state at each time point, identify the time point at which the specified eigenstate exhibits the lowest distance from the initial state for both Chebyshev and Euclidean distances, and return the time points and corresponding distances.
"""

import pandas as pd
import numpy as np

def find_min_distance_time(chebyshev_data, sqeuclidean_data, eigenstate):
    # Calculate Chebyshev distance from the initial state
    chebyshev_distances = np.abs(chebyshev_data[eigenstate] - chebyshev_data[eigenstate].iloc[0])

    # Calculate Euclidean distance from the initial state
    sqeuclidean_distances = np.sqrt(np.square(sqeuclidean_data[eigenstate] - sqeuclidean_data[eigenstate].iloc[0]))

    # Find the time point with the lowest Chebyshev distance
    min_chebyshev_distance_time = chebyshev_data['time'].iloc[chebyshev_distances.idxmin()]
    min_chebyshev_distance = chebyshev_distances.min()

    # Find the time point with the lowest Euclidean distance
    min_sqeuclidean_distance_time = sqeuclidean_data['time'].iloc[sqeuclidean_distances.idxmin()]
    min_sqeuclidean_distance = sqeuclidean_distances.min()

    return (min_chebyshev_distance_time, min_chebyshev_distance), (min_sqeuclidean_distance_time, min_sqeuclidean_distance)