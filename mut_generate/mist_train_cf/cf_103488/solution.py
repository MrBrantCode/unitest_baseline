"""
QUESTION:
Create a function `sort_descending` that takes an array of integers as input, sorts it in descending order, and returns the sorted array. The function should be able to handle an array of any size.
"""

def sort_descending(arr):
    arr.sort(reverse=True)
    return arr