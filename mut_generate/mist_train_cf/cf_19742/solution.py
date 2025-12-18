"""
QUESTION:
Write a function named `filter_primes` that takes a list of integers as input, returns a list of prime numbers in ascending order, and removes duplicates.
"""

def filter_primes(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = set(num for num in numbers if is_prime(num))
    return sorted(primes)