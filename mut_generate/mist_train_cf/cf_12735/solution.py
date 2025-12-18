"""
QUESTION:
Write a function named `largest_prime_number` that takes an array of integers as input and returns the largest prime number in the array. If no prime numbers are found, the function should return `None`.
"""

import math

def largest_prime_number(array):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    largest_prime = None
    for num in array:
        if is_prime(num):
            if largest_prime is None or num > largest_prime:
                largest_prime = num
    return largest_prime