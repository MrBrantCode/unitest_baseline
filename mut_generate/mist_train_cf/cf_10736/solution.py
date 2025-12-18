"""
QUESTION:
Write a function `sum_even_numbers_greater_than_2` that takes a list of integers as input and returns the sum of all numbers in the list that are greater than 2 and divisible by 2.
"""

def sum_even_numbers_greater_than_2(numbers):
    """
    This function calculates the sum of all numbers in the list that are greater than 2 and divisible by 2.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The sum of all numbers in the list that are greater than 2 and divisible by 2.
    """
    return sum(num for num in numbers if num > 2 and num % 2 == 0)