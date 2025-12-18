"""
QUESTION:
Write a function `find_unique_primes()` that takes a list of strings representing integers as input, ignores the case sensitivity of the elements, and returns a list of unique prime numbers within the range of 1 to 100, inclusive, without duplicates.
"""

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_unique_primes():
    """Return a list of unique prime numbers within the range of 1 to 100."""
    unique_primes = set()
    for num in range(1, 101):
        if is_prime(num):
            unique_primes.add(num)
    return list(unique_primes)