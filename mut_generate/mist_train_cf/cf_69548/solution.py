"""
QUESTION:
Write a function `calculate_lcm` that takes an integer `n` as input and returns the least common multiple (LCM) of all prime numbers less than or equal to `n`. The function should use the Sieve of Eratosthenes algorithm to find the prime numbers and then calculate their LCM.
"""

def calculate_lcm(n):
    primes = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    prime_nums = []
    for p in range(2, n+1):
        if primes[p]:
            prime_nums.append(p)
    lcm = 1
    for i in prime_nums:
        lcm *= i
    return lcm