"""
QUESTION:
Write a function `get_primes(n)` to find all prime numbers between 0 and `n` (inclusive), without using explicit looping constructs like for, while, or do-while.
"""

def get_primes(n):
    """Return a list of prime numbers between 0 and n (inclusive)."""
    
    def is_prime(num):
        """Check if a number is prime."""
        if num < 2:
            return False
        return all(num % i for i in range(2, int(num ** 0.5) + 1))

    return list(filter(is_prime, range(n + 1)))