"""
QUESTION:
Create a function called `max_abs_difference` that takes a numpy array as input and returns the maximum absolute difference of any two elements in the array. The difference is calculated by subtracting the smaller element from the larger element.
"""

import numpy as np

def max_abs_difference(arr):
    # Find the maximum and minimum values in the array
    max_val = np.max(arr)
    min_val = np.min(arr)
    
    # Calculate the maximum absolute difference
    max_diff = np.abs(max_val - min_val)
    
    return max_diff