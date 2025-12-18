"""
QUESTION:
Write a function named `sum_odd_numbers` that calculates the sum of all odd numbers in a given list of integers. The input will be a list of integers and the output should be the sum of the odd numbers in the list.
"""

def sum_odd_numbers(numbers):
    """
    This function calculates the sum of all odd numbers in a given list of integers.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The sum of the odd numbers in the list.
    """
    return sum(num for num in numbers if num % 2 != 0)