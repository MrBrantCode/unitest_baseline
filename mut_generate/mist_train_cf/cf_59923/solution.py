"""
QUESTION:
Write a function named `percentile_diff` that takes an array of numbers as input, calculates the 60th percentile and the 40th percentile of the array, and returns their difference. The function should handle any array of numbers.
"""

import numpy as np

def percentile_diff(data):
    # Calculate 60th percentile
    p60 = np.percentile(data, 60)
    
    # Calculate 40th percentile
    p40 = np.percentile(data, 40)
    
    # Find and return the difference
    return p60 - p40