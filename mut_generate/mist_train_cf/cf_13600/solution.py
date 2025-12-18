"""
QUESTION:
Write a function named `average_absolute_values` that takes a list of integers as input and returns the average of the absolute values of the non-negative numbers in the list.
"""

def average_absolute_values(numbers):
    """
    This function calculates the average of the absolute values of non-negative numbers in a list.

    Args:
        numbers (list): A list of integers.

    Returns:
        float: The average of the absolute values of non-negative numbers.
    """
    non_negative_numbers = [abs(num) for num in numbers if num >= 0]
    return sum(non_negative_numbers) / len(non_negative_numbers) if non_negative_numbers else 0