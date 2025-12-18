"""
QUESTION:
Design a function named `generate_primes` that takes an integer `n` as input and returns a list of all prime numbers up to `n`. The function should use the Sieve of Eratosthenes algorithm to efficiently generate prime numbers. The input `n` can be a large number (up to 1,000,000).
"""

def generate_primes(n):
    """
    Generate a list of all prime numbers up to n using the Sieve of Eratosthenes algorithm.

    Args:
    n (int): The upper limit for generating prime numbers.

    Returns:
    list: A list of prime numbers up to n.
    """
    prime = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    primes = [p for p in range(2, n + 1) if prime[p]]
    return primes