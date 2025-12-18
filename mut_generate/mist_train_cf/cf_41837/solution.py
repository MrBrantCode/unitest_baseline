"""
QUESTION:
Create a function named `sum_of_primes` that takes an integer `limit` as input and returns the sum of all prime numbers up to the given limit. The function should handle large limits efficiently.
"""

def sum_of_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for num in range(2, int(limit**0.5) + 1):
        if sieve[num]:
            for multiple in range(num**2, limit + 1, num):
                sieve[multiple] = False
    return sum(num for num in range(2, limit + 1) if sieve[num])