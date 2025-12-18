"""
QUESTION:
Write a function `prime_filter` that takes two integer parameters, `start` and `end`, and returns a list of all prime numbers within the range from `start` to `end` (inclusive). The function should have a time complexity of O(n*sqrt(n)) and a space complexity of O(n), where n is the range `end - start + 1`.
"""

def prime_filter(start, end):
    """Return list of prime numbers in a range."""
    def is_prime(n):
        """Check if a number is prime."""
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [n for n in range(start, end + 1) if is_prime(n)]
    return primes