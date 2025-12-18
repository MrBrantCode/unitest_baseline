"""
QUESTION:
Write a function `max_sum_path(arr)` that takes an array of integers `arr` as input and returns the maximum sum of a contiguous subarray within `arr`. The array can contain both positive and negative integers.
"""

def max_sum_path(arr):
    max_current = max_global = arr[0]
    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        if max_current > max_global:
            max_global = max_current
    return max_global