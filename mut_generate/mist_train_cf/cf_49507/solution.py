"""
QUESTION:
Write a function named `smallest_prime` that takes a list of integers as input and returns the smallest prime number in the list. The function should return the smallest prime number if one exists, otherwise it should handle the case when no prime number is found. The input list contains at least one element and all elements are non-negative integers.
"""

def smallest_prime(numbers):
    """Return the smallest prime number in the input list."""
    def is_prime(n):
        """Return 'True' if 'n' is a prime number. False otherwise."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [num for num in numbers if is_prime(num)]
    return min(primes) if primes else None