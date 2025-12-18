"""
QUESTION:
Create a function named `get_unique_even_numbers` that takes an array of integers as input. The function should return a new array containing only the even numbers from the input array, sorted in ascending order, and with no duplicates. If the input array is empty, return an empty array.
"""

def get_unique_even_numbers(arr):
    """Return a new array containing unique even numbers from the input array, sorted in ascending order."""
    return sorted(set([num for num in arr if num % 2 == 0]))