"""
QUESTION:
Write a function `normalize(data)` that takes a numpy array `data` as input and returns a new array where all values are normalized to lie in the range -1 to 1. Any values that are less than -0.5 should be rounded down to -1, and any values that are greater than 0.5 should be rounded up to 1.
"""

import numpy as np

def normalize(data):
    normalized_data = np.clip(data, -0.5, 0.5)  # Clip values outside -0.5 to 0.5 range
    normalized_data = np.divide(normalized_data, 0.5)  # Scale values to range -1 to 1
    normalized_data = np.round(normalized_data)  # Round values to -1 or 1
    return normalized_data