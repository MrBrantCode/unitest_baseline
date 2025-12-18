"""
QUESTION:
Write a function named calculate_average that calculates the average of all numbers in a given array. The function should take an array of integers as input and return the calculated average as a double value. The array is guaranteed to be non-empty.
"""

def calculate_average(arr):
    """Calculates the average of all numbers in a given array."""
    return sum(arr) / len(arr)