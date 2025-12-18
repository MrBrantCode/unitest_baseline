"""
QUESTION:
Write a function `generate_primes(N)` that returns the first N prime numbers. The function should start checking from 2 and only consider divisibility by previously found prime numbers to determine if a number is prime.
"""

def generate_primes(N):
    primes = []
    num = 2   # Start checking from 2
    while len(primes) < N:
        if all(num % prime != 0 for prime in primes):
            primes.append(num)
        num += 1
    return primes