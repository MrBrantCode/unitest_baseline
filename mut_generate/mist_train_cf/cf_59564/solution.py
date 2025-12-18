"""
QUESTION:
Write a function `print_primes(start, end)` that prints all prime numbers within a given range from `start` to `end` (inclusive), where a prime number is defined as a natural number greater than 1 that has no positive divisors other than 1 and the number itself. The function should use an auxiliary function `is_prime(n)` to check if a number `n` is prime.
"""

def is_prime(n):
    """
    Checks if a number n is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n < 2: 
        return False
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0: 
            return False
    return True

def print_primes(start, end):
    """
    Prints all prime numbers within a given range from start to end (inclusive).

    Args:
        start (int): The start of the range (inclusive).
        end (int): The end of the range (inclusive).
    """
    for n in range(start, end + 1): 
        if is_prime(n): 
            print(n)