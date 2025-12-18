"""
QUESTION:
Create a function `sort_array_descending` that takes an array of integers as input and returns the array sorted in descending order. The function should modify the input array in-place, if possible, and return the sorted array.
"""

def sort_array_descending(arr):
    arr.sort(reverse=True)
    return arr