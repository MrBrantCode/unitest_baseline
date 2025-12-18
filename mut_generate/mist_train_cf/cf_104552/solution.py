"""
QUESTION:
Write a function `filter_even_numbers` that takes an array of integers as input and returns a list of even numbers that are not divisible by 3, sorted in descending order.
"""

def filter_even_numbers(arr):
    """
    Returns a list of even numbers that are not divisible by 3, sorted in descending order.

    Args:
        arr (list): A list of integers.

    Returns:
        list: A list of even numbers not divisible by 3, in descending order.
    """
    return sorted([num for num in arr if num % 2 == 0 and num % 3 != 0], reverse=True)