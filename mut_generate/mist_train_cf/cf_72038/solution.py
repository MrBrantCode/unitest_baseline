"""
QUESTION:
Create a function `remove_divisible_by_three` that takes a list of integers as input and returns a new list containing only the numbers that are not divisible by 3.
"""

def remove_divisible_by_three(numbers):
    """
    This function takes a list of integers as input and returns a new list containing only the numbers that are not divisible by 3.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A new list containing only the numbers that are not divisible by 3.
    """
    return [num for num in numbers if num % 3 != 0]