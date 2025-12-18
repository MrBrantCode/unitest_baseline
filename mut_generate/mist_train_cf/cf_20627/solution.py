"""
QUESTION:
Write a function `is_prime(n)` that checks whether a number `n` is prime. Use this function to print all prime numbers in the range 0 to 100,000. The function should be efficient and handle large numbers.
"""

def is_prime(n):
    """
    Checks whether a number `n` is prime.

    Args:
    n (int): The number to check.

    Returns:
    bool: True if `n` is prime, False otherwise.
    """
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True