"""
QUESTION:
Write a function `sumOfPrimeDigits(N)` that calculates the sum of all prime digits between 1 and N (inclusive), where prime digits are 2, 3, 5, and 7, and returns the calculated sum. The function should only consider single-digit numbers and N is a positive integer.
"""

def sumOfPrimeDigits(N):
    """
    Calculates the sum of all prime digits between 1 and N (inclusive).

    Args:
    N (int): A positive integer.

    Returns:
    int: The sum of prime digits between 1 and N.
    """
    sum = 0
    for digit in range(1, N+1):
        if digit in [2, 3, 5, 7]:
            sum += digit
    return sum