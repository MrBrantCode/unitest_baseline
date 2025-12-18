"""
QUESTION:
Implement a function called `sum_numbers` that takes a list of integers as input. The function should return the sum of all numbers in the list that are non-negative and not divisible by 3.
"""

def sum_numbers(numbers):
    """
    This function calculates the sum of all non-negative numbers in the input list 
    that are not divisible by 3.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The sum of non-negative numbers not divisible by 3.
    """
    return sum(num for num in numbers if num >= 0 and num % 3 != 0)