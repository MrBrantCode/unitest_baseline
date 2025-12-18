"""
QUESTION:
Write a function called `count_primes(n)` to return the count of all prime numbers from 1 to `n` (inclusive) where `n` is a positive integer greater than or equal to 2.
"""

def count_primes(n):
    # Create a boolean array "is_prime[0..n]" and initialize
    # all entries it as true.
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= n:
        # If is_prime[p] is not changed, then it is a prime
        if is_prime[p] == True:
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                is_prime[i] = False
        p += 1

    # Count all prime numbers
    return sum(is_prime)