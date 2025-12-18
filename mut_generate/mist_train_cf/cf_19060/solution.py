"""
QUESTION:
Write a Python function named `sum_primes` that uses recursion to find the sum of all prime numbers within a given range from `start` to `end` (inclusive). The function should return the sum of prime numbers in the given range.
"""

def sum_primes(start, end):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    if start > end:
        return 0
    if is_prime(start):
        return start + sum_primes(start + 1, end)
    return sum_primes(start + 1, end)