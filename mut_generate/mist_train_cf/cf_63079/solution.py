"""
QUESTION:
Write a function `find_second_highest(arr)` that takes a two-dimensional array of integers as input and returns the second highest unique integer across all arrays. The function should handle arrays of different lengths and return "No second highest unique integer exists" if there is no second highest unique integer.
"""

from itertools import chain

def find_second_highest(arr):
    # Flattening the 2d array into 1d array
    flattened_arr = list(chain(*arr))
    # Removing duplicates 
    unique_arr = list(set(flattened_arr))
    # Sorting the array
    unique_arr.sort()
    # Returning the second highest integer
    if len(unique_arr) >= 2:  # to avoid 'list index out of range' error 
        return unique_arr[-2]
    else:
        return "No second highest unique integer exists"