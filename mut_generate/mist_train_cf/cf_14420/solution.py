"""
QUESTION:
Write a function `get_odd_numbers` that takes a list of integers as input, returns a new list containing only the odd numbers from the original list, and sorts them in ascending order. The input list can contain any number of integers.
"""

def get_odd_numbers(numbers):
    """
    Returns a new list containing only the odd numbers from the input list, sorted in ascending order.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A list of odd numbers in ascending order.
    """
    return sorted([num for num in numbers if num % 2 != 0])