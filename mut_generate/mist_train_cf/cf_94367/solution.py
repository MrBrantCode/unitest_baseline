"""
QUESTION:
Write a function `sum_of_divisible_primes` that calculates the sum of elements in an array that are divisible by both 2 and 3, and are prime numbers. The function should take an array of integers as input and return the sum of the specified elements.
"""

import math

def sum_of_divisible_primes(arr):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    return sum(num for num in arr if num % 2 == 0 and num % 3 == 0 and is_prime(num))