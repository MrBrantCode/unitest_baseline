"""
QUESTION:
Implement a function `find_prime_between(x, y)` that takes two positive integers `x` and `y` as input where `x < y`, and returns a prime number between `x` and `y` that is not divisible by 2, 3, 5, or 7. The solution should use the Sieve of Eratosthenes algorithm.
"""

def find_prime_between(x, y):
    def sieve_of_eratosthenes(limit):
        primes = [True] * (limit+1)
        primes[0] = primes[1] = False
        for i in range(2, int(limit**0.5)+1):
            if primes[i]:
                for j in range(i*i, limit+1, i):
                    primes[j] = False
        return [i for i in range(2, limit+1) if primes[i] and i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0]

    primes = sieve_of_eratosthenes(y)
    primes = [p for p in primes if p > x]
    return primes[0]