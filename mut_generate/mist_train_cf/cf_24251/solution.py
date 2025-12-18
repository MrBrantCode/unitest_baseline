"""
QUESTION:
Create a function `sum_factors_of_N(N)` that calculates the sum of all factors of a given positive integer `N`. The function should return the sum of all numbers that divide `N` without leaving a remainder.
"""

def sum_factors_of_N(N):
    """
    Calculate the sum of all factors of a given positive integer N.

    Args:
        N (int): A positive integer.

    Returns:
        int: The sum of all numbers that divide N without leaving a remainder.
    """
    sum = 0
    for i in range(1, N+1):
        if N % i == 0:
            sum += i
    return sum