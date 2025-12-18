"""
QUESTION:
Write a function called `calculate_statistics` that takes an array of integers as input and calculates the mean, median, mode, and range of the array. The array will always have at least one element and can have both positive and negative integers. If there is more than one mode, any of them can be considered as the mode.
"""

import statistics

def calculate_statistics(arr):
    # Mean
    mean = sum(arr) / len(arr)

    # Median
    sorted_arr = sorted(arr)
    n = len(arr)
    if n % 2 == 0:
        median = (sorted_arr[n // 2 - 1] + sorted_arr[n // 2]) / 2
    else:
        median = sorted_arr[n // 2]

    # Mode
    mode = statistics.multimode(arr)[0]

    # Range
    range_val = max(arr) - min(arr)

    return mean, median, mode, range_val