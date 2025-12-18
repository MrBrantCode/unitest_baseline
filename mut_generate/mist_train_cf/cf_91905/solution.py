"""
QUESTION:
Create a function `sieve_of_eratosthenes(n)` that takes in a positive integer `n` as input and returns a list of all prime numbers up to `n`. The function should not use any external libraries or built-in functions to check for prime numbers. The time complexity of the function should be O(n^1.5) or better, and it should handle edge cases where `n` is less than 2 by returning an empty list.
"""

def sieve_of_eratosthenes(n):
    # Edge cases
    if n < 2:
        return []

    # Create a boolean array "is_prime[0..n]" and initialize
    # all entries it as true.
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

    # Return all prime numbers
    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)

    return primes