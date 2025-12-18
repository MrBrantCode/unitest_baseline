"""
QUESTION:
Write a function called `product_of_primes(n)` that takes a positive integer `n` as input and returns the product of all prime numbers up to and including `n`. The function should use an efficient algorithm with optimal time and space complexity.
"""

def product_of_primes(n):
    primes = [True for i in range(n+1)]
    p = 2
    while(p * p <= n):
        if (primes[p] == True):
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    prime_product = 1
    for i in range(2, n+1):
        if primes[i]:
            prime_product *= i
    return prime_product