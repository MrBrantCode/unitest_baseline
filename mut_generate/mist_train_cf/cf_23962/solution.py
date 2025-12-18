"""
QUESTION:
Write a function `prime_factorize(n)` that takes an integer `n` as input and returns a list of its prime factors. The function should only consider the prime factors of `n`, not their multiplicities.
"""

def prime_factors(n):
    '''This function takes in a number and returns all the prime factors.'''
    primes = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            primes.append(i)
            n //= i
        i += 1
    if n > 1:
        primes.append(n)
    return list(set(primes))