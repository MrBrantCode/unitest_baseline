"""
QUESTION:
Create a function named `filter_and_sort` that takes an array of integers as input and returns a new array containing only the positive numbers greater than 10, sorted in ascending order.
"""

def filter_and_sort(arr):
    """Return a new array containing only the positive numbers greater than 10, sorted in ascending order."""
    return sorted([num for num in arr if num > 10])