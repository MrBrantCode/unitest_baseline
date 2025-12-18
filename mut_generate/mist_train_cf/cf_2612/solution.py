"""
QUESTION:
Write a function `calculate_sum` that takes an integer `n` as input and returns the sum of all odd integers from 1 to `n` (inclusive) while complying with PEP8 standards and optimizing for efficiency.
"""

def calculate_sum(n):
    """
    Calculate the sum of all odd integers from 1 to n (inclusive).

    Args:
        n (int): The upper limit of the range.

    Returns:
        int: The sum of all odd integers in the range.
    """
    sum_odd = 0
    for i in range(1, n+1, 2):
        sum_odd += i
    return sum_odd