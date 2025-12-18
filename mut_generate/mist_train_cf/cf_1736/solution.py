"""
QUESTION:
Write a function named `array_stats` that takes a list of integers as input and returns the mean, median, mode, range, and standard deviation of the list. The input list is guaranteed to have at least 5 elements.
"""

import statistics

def array_stats(arr):
    mean = sum(arr) / len(arr)
    arr.sort()
    median = arr[len(arr)//2] if len(arr) % 2 != 0 else (arr[len(arr)//2 - 1] + arr[len(arr)//2]) / 2
    mode = statistics.mode(arr)
    range_val = max(arr) - min(arr)
    std_dev = statistics.stdev(arr)
    return mean, median, mode, range_val, std_dev