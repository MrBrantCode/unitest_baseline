"""
QUESTION:
Write a function named `count_primes` that takes an integer `n` as input, where `n` is a positive integer greater than or equal to 2. The function should return the count of all prime numbers from 1 to `n` (inclusive) without using any built-in prime number libraries or functions.
"""

def count_primes(n):
    # Create a boolean array "is_prime[0..n]" and initialize
    # all entries as true. A value in is_prime[i] will finally
    # be false if i is not a prime, else true.
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= n:
        # If is_prime[p] is not changed, then it is a prime
        if is_prime[p]:
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    # Count the number of primes
    count = 0
    for i in range(2, n + 1):
        if is_prime[i]:
            count += 1

    return count