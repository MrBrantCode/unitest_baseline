"""
QUESTION:
Create a function named "filter_even_numbers" that takes a list of integers as input and returns a new list containing only the even numbers. The function should have an optional boolean argument "include_zero" (default value is False) that determines whether to include 0 in the output list if it is present in the input list.
"""

def filter_even_numbers(numbers, include_zero=False):
    """
    Filter the odd numbers from the list of numbers and
    returns a new list containing only the even numbers.

    Args:
    numbers (list): A list of integers.
    include_zero (bool): Optional boolean parameter to include 0 in the result list.

    Returns:
    A new list containing only the even numbers.
    """
    return [num for num in numbers if (num % 2 == 0 and num != 0) or (num == 0 and include_zero)]