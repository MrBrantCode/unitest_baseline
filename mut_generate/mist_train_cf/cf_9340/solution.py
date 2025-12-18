"""
QUESTION:
Create a function named `sum_even_numbers` that takes a list of integers as input and returns the sum of all even numbers in the list. The function should not use any built-in sum functions.
"""

def sum_even_numbers(numbers):
    """
    This function calculates the sum of all even numbers in a given list.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The sum of all even numbers in the list.
    """
    sum_even = 0
    for num in numbers:
        if num % 2 == 0:
            sum_even += num
    return sum_even