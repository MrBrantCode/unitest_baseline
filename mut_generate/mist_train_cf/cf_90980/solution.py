"""
QUESTION:
Design a function `compute_median` that takes an array of integers as input and returns the median of the array. The array length is guaranteed to be an odd number greater than 1 and may contain duplicate elements. The function should have a time complexity of O(nlogn) and a space complexity of O(1).
"""

def compute_median(arr):
    n = len(arr)
    arr.sort()  # Sort the array in non-decreasing order

    mid = n // 2
    median = arr[mid]

    return median