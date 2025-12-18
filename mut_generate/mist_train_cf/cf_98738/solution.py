"""
QUESTION:
Create a function named `is_prime(n)` that uses the Sieve of Eratosthenes algorithm to check if a given integer `n` is a prime number or not. The function should return a boolean indicating whether `n` is prime or not. The algorithm should create a comprehensive table of all integers up to `n` and label all composites (non-primes) by identifying all multiples of each prime. Optimize the function to only check up to the square root of `n` for efficiency.
"""

def is_prime(n):
    if n < 2:
        return False
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i*i:n+1:i] = [False] * len(primes[i*i:n+1:i])
    return primes[n]