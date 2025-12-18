"""
QUESTION:
Create a function called `generate_primes(n)` that takes an integer `n` as input and returns a list of all prime numbers from 2 to `n`. The function should use the Sieve of Eratosthenes algorithm and have a time complexity of O(n log log n).
"""

def generate_primes(n):
    primes = []
    sieve = [True] * (n+1)
    for curr in range(2, n+1):
        if sieve[curr]:
           primes.append(curr)
           for multiple in range(curr*2, n+1, curr):
               sieve[multiple] = False
    return primes