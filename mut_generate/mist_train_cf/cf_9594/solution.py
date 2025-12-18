"""
QUESTION:
Design a function `compute_median(arr)` that calculates the median of an array of n integers, where n is an odd number greater than 1. The array may contain duplicate elements. The function should have a time complexity of O(nlogn) and a space complexity of O(1).
"""

def compute_median(arr):
    n = len(arr)
    arr.sort()  # Sort the array in non-decreasing order

    if n % 2 == 0:  # If n is even
        mid = n // 2
        median = (arr[mid - 1] + arr[mid]) / 2
    else:  # If n is odd
        mid = n // 2
        median = arr[mid]

    return median