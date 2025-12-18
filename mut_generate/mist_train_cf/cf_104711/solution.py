"""
QUESTION:
Write a function named `sum_numbers` that takes a list of integers as input and returns the sum of all numbers in the list, excluding numbers that are divisible by either 3 or 5, but including numbers that are divisible by both 3 and 5.
"""

def sum_numbers(numbers):
    """
    This function calculates the sum of numbers in a list, excluding numbers 
    that are divisible by either 3 or 5, but including numbers that are 
    divisible by both 3 and 5.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The sum of the numbers in the list, following the specified rules.
    """
    total_sum = 0
    for num in numbers:
        if (num % 3 == 0 and num % 5 == 0) or (num % 3 != 0 and num % 5 != 0):
            total_sum += num
    return total_sum