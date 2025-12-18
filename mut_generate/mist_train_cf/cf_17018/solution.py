"""
QUESTION:
Write a function `find_median` that takes an array of integers as input and returns the median of the array. The array may contain duplicate values. The function should handle both even and odd length arrays.
"""

def find_median(arr):
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    if n % 2 == 0:
        return (sorted_arr[n//2] + sorted_arr[n//2 - 1]) / 2
    else:
        return sorted_arr[n//2]