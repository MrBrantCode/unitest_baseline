"""
QUESTION:
Write a function `sum_odd_numbers` to calculate the sum of all odd numbers within a given range from 1 to n using a while loop in Python. The function should take an integer n as input and return the sum of odd numbers.
"""

def sum_odd_numbers(n):
    """
    Calculate the sum of all odd numbers within a given range from 1 to n using a while loop.

    Args:
        n (int): The upper limit of the range.

    Returns:
        int: The sum of odd numbers.
    """
    sum_of_odd_numbers = 0
    num = 1

    while num <= n:
        if num % 2 != 0:
            sum_of_odd_numbers += num
        num += 1

    return sum_of_odd_numbers