"""
QUESTION:
Write a function `sum_even_numbers` that takes a list of integers as input and returns the sum of all even numbers that are greater than or equal to 10 in the list.
"""

def sum_even_numbers(numbers):
    """
    This function calculates the sum of all even numbers that are greater than or equal to 10 in the given list.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The sum of even numbers greater than or equal to 10.
    """
    total_sum = sum(num for num in numbers if num % 2 == 0 and num >= 10)
    return total_sum