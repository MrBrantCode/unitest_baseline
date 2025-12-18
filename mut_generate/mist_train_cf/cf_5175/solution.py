"""
QUESTION:
Create a function `sieve_of_eratosthenes(n)` that returns a list of all prime numbers up to `n`. The function should have a time complexity of less than O(n^2) and a space complexity of less than O(n).
"""

def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    
    result = []
    for i in range(2, n+1):
        if primes[i]:
            result.append(i)
    
    return result