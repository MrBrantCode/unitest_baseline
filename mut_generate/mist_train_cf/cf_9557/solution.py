"""
QUESTION:
Write a function named `find_largest_prime` that takes a list of positive integers as input and returns the largest prime number in the list. If the list does not contain any prime numbers, the function should return `None`.
"""

import math

def find_largest_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    for num in reversed(numbers):
        if is_prime(num):
            return num
    return None