"""
QUESTION:
Write a function called `count_primes(n)` that takes an integer `n` as input and returns the number of prime numbers from 1 to `n`.
"""

def count_primes(n):
    primes = [False, False] + [True for i in range(n-1)]
    p = 2
    while (p * p <= n):
        if primes[p] == True:
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    
    count = 0
    for i in range(2, n+1):
        if primes[i]:
            count += 1
    return count