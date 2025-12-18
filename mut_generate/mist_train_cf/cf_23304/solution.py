"""
QUESTION:
Create a function `is_prime(n)` that determines whether a given number `n` is a prime number or not. A prime number is only divisible by 1 and itself. The function should take an integer `n` as input and return a boolean value indicating whether `n` is prime or not.
"""

def is_prime(n):
    """
    Checks if a given number is a prime number.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True