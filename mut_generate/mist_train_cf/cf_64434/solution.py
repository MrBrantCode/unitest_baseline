"""
QUESTION:
Create a function `segment_and_compute_mean` that takes a 1D numpy array `data` and an integer `segment_size` as input, and returns a 1D numpy array where each element is the mean of a segment of `data` of length `segment_size`. If the length of `data` is not a multiple of `segment_size`, the remaining elements are discarded.
"""

import numpy as np

def segment_and_compute_mean(data, segment_size):
    n_segments = len(data) // segment_size
    segmented_data = data[:n_segments*segment_size].reshape(n_segments, segment_size)
    return segmented_data.mean(axis=1)