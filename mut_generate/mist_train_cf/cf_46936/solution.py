"""
QUESTION:
Create a function named `separate_odd_numbers` that takes an array of integers as input, separates the odd numbers, and returns them in a new array without using any explicit loops, with a time complexity of O(n).
"""

def separate_odd_numbers(array):
    """Separates the odd numbers from the input array and returns them in a new array."""
    return list(filter(lambda x: x % 2 != 0, array))