"""
QUESTION:
Write a function `max_decreasing_subarray` that takes a list of integers as input and returns the longest subarray where each element is one smaller than the previous one. The function should return the subarray with the maximum length.
"""

def max_decreasing_subarray(arr):
    longest_start = longest_end = prev_start = 0
    for i in range(1, len(arr)):
        if arr[i-1] - arr[i] != 1:
            if i - prev_start > longest_end - longest_start:
                longest_start, longest_end = prev_start, i
            prev_start = i
    if len(arr) - prev_start > longest_end - longest_start:
        longest_start, longest_end = prev_start, len(arr)
    return arr[longest_start:longest_end]