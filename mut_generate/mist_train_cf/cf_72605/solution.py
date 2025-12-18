"""
QUESTION:
Create a function `sort_descending` that takes an array of numerical values as input, and returns the array with its elements rearranged in descending order.
"""

def sort_descending(arr):
    arr.sort(reverse=True)
    return arr