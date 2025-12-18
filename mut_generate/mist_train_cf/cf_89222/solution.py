"""
QUESTION:
Write a function `sieve_of_eratosthenes` that takes a limit as input and returns a list of prime numbers up to that limit. The function should be able to handle large limits (up to 100,000) and run in under 1 second. The output list should contain unique prime numbers only.
"""

def sieve_of_eratosthenes(limit):
    primes = [True] * (limit+1)
    primes[0] = primes[1] = False

    p = 2
    while p*p <= limit:
        if primes[p]:
            for i in range(p*p, limit+1, p):
                primes[i] = False
        p += 1

    return [i for i in range(limit+1) if primes[i]]