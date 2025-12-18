"""
QUESTION:
Write a function `find_median` that takes an array of integers as input and returns the median of the array. The array will always have an odd number of elements and may contain duplicate values. The function should return a single integer value, which is the median of the array.
"""

def find_median(arr):
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    return sorted_arr[n//2]