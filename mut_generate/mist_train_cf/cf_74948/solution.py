"""
QUESTION:
Implement a function named **custom_prime_sieve** that generates a list of prime numbers up to a given integer N (1 < N <= 1,000,000) using the Sieve of Eratosthenes algorithm. The function should take an integer N as input and return a list of prime numbers up to N.
"""

def custom_prime_sieve(N):
    sieve = [True] * (N+1)
    p = 2
    while (p * p <= N):

        # If sieve[p] is not changed, then it is a prime
        if (sieve[p] == True):

            # Update all multiples of p
            for i in range(p * p, N+1, p):
                sieve[i] = False
        p += 1
    primes = [p for p in range(2, N) if sieve[p]]
    return primes