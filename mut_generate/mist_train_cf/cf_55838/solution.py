"""
QUESTION:
Implement a function `generate_primes(n)` that generates all prime numbers between 2 and `n` (inclusive), where `n` is a positive integer. The function should return a list of prime numbers in ascending order. The time complexity of the solution should be more efficient than O(n sqrt(n)).
"""

def generate_primes(n):
    primes = [True for i in range(n+1)]
    p = 2
    while(p*p <= n):
        if primes[p] == True:
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1

    prime_nums = [p for p in range(2, n) if primes[p]]
    
    return prime_nums