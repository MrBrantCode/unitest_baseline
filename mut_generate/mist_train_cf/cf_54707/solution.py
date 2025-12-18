"""
QUESTION:
Write a function named `sort_descending` that takes an array of floating point numbers as input and returns the array sorted in descending order.
"""

def sort_descending(arr):
    # Use the sort() function built into lists
    # Reverse the list because sort() orders from smallest to largest
    arr.sort(reverse=True)
    return arr