"""
QUESTION:
Create a function `sort_numbers(numbers)` that takes a list of numbers as input and returns the list sorted in such a way that all non-prime numbers come first, followed by prime numbers in descending order.
"""

import math

def sort_numbers(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    primes = [num for num in numbers if is_prime(num)]
    non_primes = [num for num in numbers if not is_prime(num)]
    return non_primes + sorted(primes, reverse=True)