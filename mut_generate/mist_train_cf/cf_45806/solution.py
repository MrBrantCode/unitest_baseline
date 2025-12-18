"""
QUESTION:
Create a function named is_prime(n) that determines whether a given integer n is prime or not, returning True for prime numbers and False for non-primes. The function should work for all positive integers, including edge cases such as numbers less than or equal to 1, and must be efficient for large inputs.
"""

def is_prime(n):
    """Returns true for prime integers, and false for non-primes."""
    # Corner cases
    if n <= 1:
        return False
    if n <= 3:
        return True

    # This is checked so that we can skip middle five numbers in below loop
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True