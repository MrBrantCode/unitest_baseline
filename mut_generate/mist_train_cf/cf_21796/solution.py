"""
QUESTION:
Create a function named `filter_primes` that takes a tuple of integers as input and returns a new tuple containing only the prime numbers from the original tuple.
"""

def filter_primes(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return tuple(filter(is_prime, numbers))