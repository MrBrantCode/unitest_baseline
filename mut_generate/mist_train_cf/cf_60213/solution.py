"""
QUESTION:
Write a function named `is_prime()` that takes an integer as input and returns True if the integer is prime and False otherwise. Use this function to find and count the prime numbers in a given sequence. The function should be able to handle a sequence of integers. The function should print out the list of prime numbers and the count of prime numbers.
"""

def is_prime(n):
    """Returns True if n is a prime number, False otherwise."""
    if n < 2:
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