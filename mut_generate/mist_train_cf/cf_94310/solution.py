"""
QUESTION:
Write a function called `remove_duplicates` that takes a NumPy array of positive integers as input, removes all duplicate elements, and returns the resulting array in ascending order.
"""

import numpy as np

def remove_duplicates(arr):
    unique_elements, _ = np.unique(arr, return_counts=True)
    return np.sort(unique_elements)