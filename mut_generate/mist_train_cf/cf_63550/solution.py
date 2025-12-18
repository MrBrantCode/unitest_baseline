"""
QUESTION:
Design a function `find_median(values)` that takes a list of five unique numbers as input, sorts them, and returns their median. Assume the input list will always contain an odd number of elements.
"""

def find_median(values):
    # First, we sort the values
    sorted_values = sorted(values)

    # Then, we find the median 
    median_idx = len(sorted_values) // 2

    return sorted_values[median_idx]