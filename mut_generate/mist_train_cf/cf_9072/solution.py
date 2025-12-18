"""
QUESTION:
Create a function `sort_array_descending(arr)` that takes an array of integers as input, sorts the elements in descending order, and returns the sorted array.
"""

def sort_array_descending(arr):
    arr.sort(reverse=True)
    return arr