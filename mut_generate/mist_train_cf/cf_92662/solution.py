"""
QUESTION:
Write a function `add_odd_primes` that takes an array of integers as input and returns the sum of all odd prime numbers in the array. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The input array can contain any integers (positive, negative, or zero).
"""

import math

def add_odd_primes(arr):
    """
    Returns the sum of all odd prime numbers in the given array.

    Args:
        arr (list): A list of integers.

    Returns:
        int: The sum of all odd prime numbers in the array.
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    return sum(num for num in arr if num % 2 != 0 and is_prime(num))