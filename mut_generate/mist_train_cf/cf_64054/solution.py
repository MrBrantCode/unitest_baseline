"""
QUESTION:
Write a function `sort_descending(arr)` that takes an array of integers as input and returns the array sorted in descending order. The array can contain any number of integers, and the function should return a new array with the same integers in descending order.
"""

def sort_descending(arr):
    return sorted(arr, reverse=True)