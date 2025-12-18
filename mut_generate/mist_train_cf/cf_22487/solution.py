"""
QUESTION:
Write a function named `sum_odd_numbers` that calculates and returns the sum of all odd numbers in a given range from 1 to n (inclusive), where n is a positive integer. The function should take an integer n as input and return the sum as output.
"""

def sum_odd_numbers(n):
    """
    This function calculates the sum of all odd numbers in a given range from 1 to n (inclusive).

    Args:
    n (int): A positive integer.

    Returns:
    int: The sum of all odd numbers between 1 and n (inclusive).
    """
    sum_odd = 0
    for num in range(1, n + 1):
        if num % 2 != 0:
            sum_odd += num
    return sum_odd