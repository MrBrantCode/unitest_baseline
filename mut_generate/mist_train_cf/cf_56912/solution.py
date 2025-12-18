"""
QUESTION:
Create a function named `countPrimes` that takes an integer `n` as input and returns two integers. The first integer is the count of prime numbers less than `n`, and the second integer is the sum of these prime numbers. The function should work for `0 <= n <= 5 * 10^6`.
"""

def countPrimes(n):
    
    if n < 2:
        return 0, 0
    
    primes = [0, 0] + [1] * (n-2)
    p = 2
    while p * p <= n:
        if primes[p] == 1:
            for i in range(p*p, n, p):
                primes[i] = 0
        p += 1
    
    prime_numbers = [p for p, is_prime in enumerate(primes) if is_prime]
    return len(prime_numbers), sum(prime_numbers)