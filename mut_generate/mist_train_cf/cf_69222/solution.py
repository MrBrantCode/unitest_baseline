"""
QUESTION:
Implement the `fibonacci_primes` function, which takes an integer `n` as input and returns a list of prime Fibonacci numbers up to the `n`-th Fibonacci number. The function should use the Segmented Sieve of Eratosthenes to efficiently generate prime numbers. Note that the input `n` can be large, so an optimized implementation is required.
"""

import math

def fibonacci_primes(n):
    if n<=0:
        return []
    fib = [0, 1]
    fib_primes_list = []
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    primes = [True]*(fib[-1]+1)
    primes[0] = primes[1] = False
    p = 2
    while(p * p <= fib[-1]):
        if(primes[p]):
            for i in range(p * 2, fib[-1]+1, p):
                primes[i] = False
        p += 1
    primes = [p for p in range(2, fib[-1]+1) if primes[p]]
    for num in fib:
        if num in primes:
            fib_primes_list.append(num)
    return fib_primes_list