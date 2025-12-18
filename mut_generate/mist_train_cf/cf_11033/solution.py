"""
QUESTION:
Write a function named `sum_natural_numbers` that calculates the sum of the first n natural numbers. The function should take an integer n as input and return the sum. Use the formula for the sum of an arithmetic series to solve the problem.
"""

def sum_natural_numbers(n):
    """
    Calculate the sum of the first n natural numbers.

    Args:
        n (int): The number of natural numbers to sum.

    Returns:
        int: The sum of the first n natural numbers.
    """
    return (n / 2) * (1 + n)