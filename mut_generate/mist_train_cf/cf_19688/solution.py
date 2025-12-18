"""
QUESTION:
Write a function called `calculate_mean` that calculates the mean of a list of numbers. The function should take a list of integers as input, handle duplicate numbers, and return the mean rounded to the nearest integer value.
"""

def calculate_mean(numbers):
    """
    Calculate the mean of a list of numbers.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The mean of the numbers rounded to the nearest integer value.
    """
    return round(sum(set(numbers)) / len(set(numbers)))