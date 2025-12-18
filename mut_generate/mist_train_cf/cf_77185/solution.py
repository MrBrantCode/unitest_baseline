"""
QUESTION:
Write a function `sort_odd_numbers` that takes an array of integers as input and returns the array sorted in descending order. The input array will only contain odd numbers.
"""

def sort_odd_numbers(numbers):
    """
    Sorts an array of odd integers in descending order.

    Args:
    numbers (list): A list of odd integers.

    Returns:
    list: The sorted list in descending order.
    """
    return sorted(numbers, reverse=True)