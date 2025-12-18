"""
QUESTION:
Create a function `max_variance(arr1, arr2)` that calculates and returns the maximum variance between two input arrays `arr1` and `arr2`. The function should accept two lists of numbers as input and return a single number representing the maximum variance.
"""

import numpy as np

def max_variance(arr1, arr2): 
    """Return the maximum variance between two arrays."""
    variance1 = np.var(arr1)
    variance2 = np.var(arr2)
    
    return max(variance1, variance2)