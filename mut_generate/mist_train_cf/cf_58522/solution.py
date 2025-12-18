"""
QUESTION:
Implement a function `is_prime(n)` that checks if a number `n` is prime, with the condition that the function must handle both positive and negative integers, and must return a boolean value.
"""

def is_prime(n):
    """
    Checks if a number is prime.

    Args:
    n (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True