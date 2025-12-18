"""
QUESTION:
Write a function called `calculate_statistics` that takes a list of numbers as input and returns the maximum, minimum, average, and sum of the numbers. The function should handle a list of at least one element.
"""

def calculate_statistics(numbers):
    """
    Calculate the maximum, minimum, average, and sum of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        dict: A dictionary containing the maximum, minimum, average, and sum of the numbers.
    """
    maximum = max(numbers)
    minimum = min(numbers)
    average = sum(numbers) / len(numbers)
    summation = sum(numbers)

    return {
        "Maximum": maximum,
        "Minimum": minimum,
        "Average": average,
        "Sum": summation
    }