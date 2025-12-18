"""
QUESTION:
Write a function named `calculate_stats` that takes a list of numbers as input and returns the maximum, minimum, and average values from the list.
"""

def calculate_stats(numbers):
    """
    Calculate the maximum, minimum, and average values from a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        tuple: A tuple containing the maximum, minimum, and average values.
    """
    max_val = max(numbers)
    min_val = min(numbers)
    avg_val = sum(numbers) / len(numbers)
    return max_val, min_val, avg_val