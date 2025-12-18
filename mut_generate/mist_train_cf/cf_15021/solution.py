"""
QUESTION:
Write a function named `filter_even_numbers` that takes a list of integers as input and returns a new list containing only the even numbers from the input list, sorted in ascending order. The original list should remain unchanged.
"""

def filter_even_numbers(arr):
    """Return a new list containing only the even numbers from the input list, sorted in ascending order."""
    return sorted([num for num in arr if num % 2 == 0])