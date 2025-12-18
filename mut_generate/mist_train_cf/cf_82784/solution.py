"""
QUESTION:
Implement a function `primes_count(n)` that returns the first `n` prime numbers. The function should have a time complexity of no greater than O(n log log n) and should not use the standard library or any in-built methods for prime calculations. The function may assume that the input `n` is a positive integer.
"""

def primes_count(n):
    if n < 1:
        return
    primes = []
    sieve = [True] * (n*10)  
    for x in range(2, n*10):
        if sieve[x]:  
            primes.append(x)
            if len(primes) == n:  
                return primes
            for u in range(x, n*10, x):  
                sieve[u] = False