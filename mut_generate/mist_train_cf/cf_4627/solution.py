"""
QUESTION:
Write a function named `sum_of_primes` that calculates the sum of prime numbers from 2 to a given number `n`. The function must use the Sieve of Eratosthenes algorithm to generate prime numbers. The function should take an integer `n` as input and return the sum of prime numbers from 2 to `n`.
"""

def sum_of_primes(n):
    prime = [True] * (n+1)
    p = 2
    while (p**2 <= n):
        if (prime[p] == True):
            for i in range(p**2, n+1, p):
                prime[i] = False
        p += 1
    prime_sum = 0
    for i in range(2, n+1):
        if prime[i]:
            prime_sum += i
    return prime_sum