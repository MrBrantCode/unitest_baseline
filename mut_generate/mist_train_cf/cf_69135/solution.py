"""
QUESTION:
Write a function called `sieve_of_eratosthenes(n)` that takes an integer `n` and returns a list of prime integers between 2 and `n-1` using the Sieve of Eratosthenes algorithm.
"""

def sieve_of_eratosthenes(n):
    primes = [True for i in range(n+1)] 
    p = 2
    while (p**2 <= n): 
        if primes[p] == True: 
            for i in range(p**2, n+1, p): 
                primes[i] = False
        p += 1

    prime_list = [p for p in range(2, n) if primes[p]] 
    return prime_list