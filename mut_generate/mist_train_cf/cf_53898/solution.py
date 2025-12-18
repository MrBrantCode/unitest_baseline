"""
QUESTION:
Write a function called `find_max_deviation` that takes a 2D array of integers as input and returns the maximum difference between the minimum and maximum values across all sub-arrays.
"""

def find_max_deviation(arr):
    min_val = min(min(sub) for sub in arr)
    max_val = max(max(sub) for sub in arr)
    return max_val - min_val