"""
QUESTION:
Implement a function named `find_primes` that takes an integer `n` as input and returns a list of all prime numbers from 2 to `n` (inclusive). The function should use the Sieve of Eratosthenes algorithm. The input integer `n` should be a non-negative integer, and the function should return a list of integers representing the prime numbers within the specified range.
"""

def find_primes(n):
    # Create a boolean array "is_prime[0..n]" and initialize
    # all entries it as true.
    is_prime = [True] * (n + 1)
    p = 2  # Smallest prime number

    while p * p <= n:
        # If is_prime[p] is not changed, then it is a prime
        if is_prime[p]:
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    # Create a list of prime numbers
    primes = [p for p in range(2, n + 1) if is_prime[p]]

    return primes