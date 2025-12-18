"""
QUESTION:
Write a function named `sort_descending` that takes a list of numbers as input, sorts the list in descending order, and returns the first element of the sorted list.
"""

def sort_descending(nums):
    return sorted(nums, reverse=True)[0]