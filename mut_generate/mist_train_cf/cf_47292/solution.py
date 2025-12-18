"""
QUESTION:
Create a function called `primes(n)` that generates all prime numbers from 1 to `n` using the Sieve of Eratosthenes algorithm and list comprehension, with a time complexity of O(n log log n). The function should take an integer `n` as input and return a list of prime numbers.
"""

def primes(n):
    sieve = [1] * (n+1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = 0
    return [i for i in range(2, n + 1) if sieve[i]]