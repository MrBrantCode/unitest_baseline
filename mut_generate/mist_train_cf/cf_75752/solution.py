"""
QUESTION:
Write a function `max_subarray_sum` that takes an array of integers as input and returns the maximum accumulative value that can be attained from any subsequence of the input array. The function should have a time complexity of O(n), where n is the length of the input array.
"""

def max_subarray_sum(arr):
    max_current = max_global = arr[0]
    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        if max_current > max_global:
            max_global = max_current
    return max_global