"""
QUESTION:
Define a function `find_median(arr)` that calculates the median of a given array of numbers. The array is guaranteed to have an odd number of elements and must be sorted in ascending order. Implement the function without using any built-in functions, loops, or recursion, and return the middle element as the median.
"""

def find_median(arr):
    mid_index = len(arr) // 2
    return arr[mid_index]