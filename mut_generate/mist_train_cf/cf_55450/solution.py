"""
QUESTION:
Create a function named `sort_descending` that takes an array of numbers as input and returns the array sorted in descending order. The function should rearrange the elements in the array from highest to lowest value.
"""

def sort_descending(arr):
    arr.sort(reverse=True)
    return arr