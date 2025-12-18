"""
QUESTION:
Create a function named `primes_up_to_n` that generates a list of prime numbers up to the nth term. The function should take an integer `n` as input and return a list of integers.
"""

def primes_up_to_n(n):
    primes = []
    i = 2
    while len(primes) < n:
        for p in primes:
            if i % p == 0:
                break
        else:
            primes.append(i)
        i += 1
    return primes