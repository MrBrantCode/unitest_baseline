"""
QUESTION:
Create a function `sieve_of_eratosthenes(n)` that calculates the sum of all prime numbers from 1 to `n` without using any built-in or external libraries or modules. The function should be optimized to perform this task efficiently for larger ranges.
"""

def sum_of_primes(n):
    prime = [True for i in range(n+1)]
    prime_sum = 0
    p = 2
    while p**2 <= n:
        if prime[p] == True:
            for i in range(p**2, n+1, p):
                prime[i] = False
        p += 1
    for p in range(2, n):
        if prime[p]:
            prime_sum += p
    return prime_sum