"""
QUESTION:
Write a function `max_cumulative_total(arr)` that calculates the highest cumulative total of sequential elements within the provided array. The array can contain both positive and negative numbers, and the function should return the maximum sum of a contiguous subarray.
"""

def max_cumulative_total(arr):
    max_current = max_global = arr[0]
    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        if max_current > max_global:
            max_global = max_current
    return max_global