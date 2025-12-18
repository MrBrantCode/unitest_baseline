"""
QUESTION:
Write a function `sum_of_odd_numbers_multiplied_by_3` that takes a positive integer `n` as input and returns the sum of all odd numbers from 1 to `n` multiplied by 3.
"""

def sum_of_odd_numbers_multiplied_by_3(n):
    """
    Returns the sum of all odd numbers from 1 to n multiplied by 3.

    Args:
    n (int): A positive integer.

    Returns:
    int: The sum of all odd numbers from 1 to n multiplied by 3.
    """
    sum = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            sum += i
    return sum * 3