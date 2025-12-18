"""
QUESTION:
Design a function called `find_primes` that takes an integer `limit` as input and returns a list of all prime numbers up to the given `limit`. The function should also calculate and return the count and sum of the prime numbers. The input `limit` is a positive integer.
"""

def find_primes(limit):
    """Find all primes up to the given limit and return them along with their count and sum."""
    def is_prime(n):
        """Return True if n is a prime number."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    primes = [n for n in range(2, limit+1) if is_prime(n)]
    return primes, len(primes), sum(primes)