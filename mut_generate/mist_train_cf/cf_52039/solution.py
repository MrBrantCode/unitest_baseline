"""
QUESTION:
Write a function `cumsum_primes_in_range` that calculates and returns the cumulative sum of prime numbers within a given range defined by the parameters `start` and `end`, where `start` is inclusive and `end` is inclusive.
"""

def cumsum_primes_in_range(start, end):
    """Calculate cumulative sum of prime numbers in a range."""
    def is_prime(n):
        """Check if a number is a prime number."""
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i:
                i += 2
            else:
                return False
        return True

    return sum(n for n in range(start, end+1) if is_prime(n))