"""
QUESTION:
Write a recursive function `are_relatively_prime(a, b)` that takes two integers `a` and `b` as input and returns `True` if they are relatively prime (i.e., their greatest common divisor is 1) and `False` otherwise. The function should also output the prime factorization of `a` and `b` and the number of distinct prime factors they share. Use helper functions `prime_factors(n)` to calculate the prime factors of an integer `n` and `num_distinct_prime_factors(n)` to calculate the number of distinct prime factors of an integer `n`.
"""

def prime_factors(n):
    """Return a set of prime factors of n."""
    factors = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            factors.add(i)
            factors.update(prime_factors(n//i))
    if n > 1:
        factors.add(n)
    return factors

def num_distinct_prime_factors(n):
    """Return the number of distinct prime factors of n."""
    return len(prime_factors(n))

def are_relatively_prime(a, b):
    """Return True if a and b are relatively prime, False otherwise."""
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    return gcd(a, b) == 1