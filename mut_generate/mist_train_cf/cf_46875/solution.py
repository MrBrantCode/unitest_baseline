"""
QUESTION:
Write a function `largest_prime_divisor(n)` that finds the largest prime number smaller than the input number `n` that divides `n` evenly. If no such prime number exists, return -1.
"""

def largest_prime_divisor(n):
    """
    Finds the largest prime number smaller than the input number `n` that divides `n` evenly.
    If no such prime number exists, return -1.

    Args:
        n (int): The input number.

    Returns:
        int: The largest prime divisor of `n` or -1 if not found.
    """

    def is_prime(num):
        """Checks if a number is prime."""
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    if n <= 1:
        return -1
    for i in range(n - 1, 1, -1):
        if n % i == 0 and is_prime(i):
            return i
    return -1