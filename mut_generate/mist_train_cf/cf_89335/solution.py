"""
QUESTION:
Create a function named `calculate_cumulative_sum` that takes an array of integers as input, calculates the cumulative sum of the array starting from the third element (index 2), and returns the result. The array may contain negative numbers.
"""

def calculate_cumulative_sum(array):
    """
    Calculate the cumulative sum of the array starting from the third element (index 2).

    Args:
    array (list): An array of integers.

    Returns:
    int: The cumulative sum of the array starting from the third element.
    """
    cumulative_sum = 0
    for i in range(2, len(array)):
        cumulative_sum += array[i]
    return cumulative_sum