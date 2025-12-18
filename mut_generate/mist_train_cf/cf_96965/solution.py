"""
QUESTION:
Write a function `sum_excluding_multiples` that calculates the sum of numbers from 1 to n, excluding any numbers that are divisible by both a and b. The function should take three parameters: n, a, and b, and return the calculated sum.
"""

def sum_excluding_multiples(n, a, b):
    """
    Calculate the sum of numbers from 1 to n, excluding any numbers that are divisible by both a and b.

    Args:
        n (int): The upper limit of the range.
        a (int): The first divisor.
        b (int): The second divisor.

    Returns:
        int: The calculated sum.
    """
    total = 0
    for num in range(1, n + 1):
        if num % a != 0 or num % b != 0:
            total += num
    return total