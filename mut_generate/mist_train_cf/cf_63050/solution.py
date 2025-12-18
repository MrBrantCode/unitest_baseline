"""
QUESTION:
Write a function `sort_descending` that takes an array of integers as input and returns the array in descending order. The function should be able to handle arrays of varying lengths.
"""

def sort_descending(arr):
    arr.sort(reverse=True)
    return arr