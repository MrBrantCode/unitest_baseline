"""
QUESTION:
Write a function `max_diff` that takes a 2-dimensional array of integers as input and returns the maximum difference between the smallest element and the largest element in each sub-array.
"""

def max_diff(arr):
    max_difference = float('-inf')
    for sub_arr in arr:
        sub_min = min(sub_arr)
        sub_max = max(sub_arr)
        difference = sub_max - sub_min
        max_difference = max(difference, max_difference)
    return max_difference