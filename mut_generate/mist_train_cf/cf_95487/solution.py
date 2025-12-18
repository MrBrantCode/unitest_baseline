"""
QUESTION:
Write a function `sum_primes(start, end)` that uses recursion to find the sum of all prime numbers within a given range. The function should take two parameters, `start` and `end`, which represent the start and end of the range respectively, and return the sum of all prime numbers within that range.
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