"""
QUESTION:
Write a function that generates a list of prime numbers from 1 to 1000. The function should include a helper function `is_prime(n)` that checks whether a number `n` is prime or not.
"""

def is_prime(n):
    """Checks whether a number `n` is prime or not."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(n):
    """Generates a list of prime numbers from 1 to `n`."""
    prime_numbers = []
    for num in range(1, n + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers