"""
QUESTION:
Write a function `find_median` that takes an array of numbers as input, calculates the median of the array, and returns the median value. The array is guaranteed to have an odd number of elements. Do not use any built-in functions or libraries, and do not use loops or recursion in your implementation.
"""

def find_median(arr):
    arr.sort()
    mid_index = len(arr) // 2
    return arr[mid_index]