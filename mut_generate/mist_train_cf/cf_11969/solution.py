"""
QUESTION:
Write a function `count_distinct_primes(n)` that takes a positive integer `n` as input and returns the number of distinct prime numbers less than or equal to `n`. The function should be efficient and handle large inputs.
"""

def count_distinct_primes(n):
    """
    Counts the number of distinct prime numbers less than or equal to n.

    Args:
        n (int): A positive integer.

    Returns:
        int: The number of distinct prime numbers less than or equal to n.
    """
    def is_prime(num):
        """Checks whether a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = set()
    for i in range(2, n+1):
        if is_prime(i):
            primes.add(i)
    return len(primes)