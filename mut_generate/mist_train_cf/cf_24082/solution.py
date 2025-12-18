"""
QUESTION:
Write a function `sort_desc` to sort a list of integers in non-increasing order. The function should accept a list of integers as input and return a new sorted list.
"""

def sort_desc(arr):
    """Sort a list of integers in non-increasing order."""
    return sorted(arr, reverse=True)