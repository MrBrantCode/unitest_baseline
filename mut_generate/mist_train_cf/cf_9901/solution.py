"""
QUESTION:
Write a function named `find_primes` that takes an integer `n` as input and returns a list of all prime numbers up to `n`. The function should use the Sieve of Eratosthenes algorithm to optimize its performance. Note that the input `n` is an upper limit for the range of prime numbers, and you should return all prime numbers from 2 to `n` (inclusive).
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