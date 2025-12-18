"""
QUESTION:
Create a function `segmented_sieve(A, B)` that generates a list of prime numbers between two numbers A and B (both inclusive) using a segmented sieve algorithm with a time complexity of less than O((B-A+1)log(log(B))).
"""

import math

def segmented_sieve(A, B):
    # Generate all primes up to sqrt(B)
    limit = int(math.sqrt(B))
    primes = sieve(limit)

    # Create a boolean array to mark primes in the range A to B
    is_prime = [True] * (B - A + 1)

    # Mark primes in the range A to B
    for prime in primes:
        if prime <= limit:
            # Find the smallest multiple of prime in the range A to B
            start = math.ceil(A / prime) * prime
            if start == prime:
                start += prime

            # Mark all multiples of prime as non-prime
            for i in range(start, B + 1, prime):
                is_prime[i - A] = False

    # Create a list of prime numbers in the range A to B
    primes_list = []
    for i in range(A, B + 1):
        if is_prime[i - A]:
            primes_list.append(i)

    return primes_list

def sieve(n):
    # Create a boolean array "prime[0..n]" and initialize all entries as true
    prime = [True for _ in range(n+1)]
    prime[0] = prime[1] = False

    p = 2
    while p*p <= n:
        # If prime[p] is not changed, then it is a prime
        if prime[p]:
            # Update all multiples of p
            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1

    # Return a list of prime numbers
    primes = []
    for p in range(2, n+1):
        if prime[p]:
            primes.append(p)

    return primes