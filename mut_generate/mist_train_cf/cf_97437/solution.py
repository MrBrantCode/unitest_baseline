"""
QUESTION:
Write a recursive function `generate_primes` that generates a list of prime numbers within a given range, from `start` to `end` (inclusive), without using any built-in library functions to check for prime numbers.
"""

def generate_primes(start, end):
    def is_prime(n, i=2):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % i == 0:
            return False
        if i * i > n:
            return True
        return is_prime(n, i + 1)

    if start > end:
        return []
    if is_prime(start):
        return [start] + generate_primes(start + 1, end)
    return generate_primes(start + 1, end)