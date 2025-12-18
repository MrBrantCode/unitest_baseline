"""
QUESTION:
Create a function named `is_prime` that determines if a given integer `n` is a prime number or not using the Sieve of Eratosthenes algorithm. The function should only return a boolean value indicating whether the number is prime or not. The input `n` is an integer greater than 1.
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