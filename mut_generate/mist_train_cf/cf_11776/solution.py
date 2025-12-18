"""
QUESTION:
Write a function named `get_odd_numbers` that takes a list of integers as input, iterates over the list using a single loop, and returns a new list containing only the odd numbers from the original list.
"""

def get_odd_numbers(numbers):
    """
    This function takes a list of integers, iterates over the list, 
    and returns a new list containing only the odd numbers from the original list.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A new list containing only the odd numbers.
    """
    result = []
    for num in numbers:
        if num % 2 == 1:
            result.append(num)
    return result