"""
QUESTION:
Create a function called `find_primes(n)` that takes an integer `n` as input and returns a dictionary containing prime numbers between 0 and `n` as keys and their frequency as values. The function should be optimized to handle large values of `n`.
"""

def find_primes(n):
    primes = {}
    sieve = [1] * (n + 1)
    for x in range(2, n + 1):
        if sieve[x]:  
            primes[x] = 1
            for u in range(x, n + 1, x):  
                sieve[u] = 0
    return primes