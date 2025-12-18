"""
QUESTION:
Write a function `are_all_primes` that takes a list of numbers as input and returns `True` if all numbers in the list are prime, and `False` otherwise. The time complexity of the function should be less than O(n^2), where n is the length of the input list.
"""

import math

def are_all_primes(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    for num in numbers:
        if not is_prime(num):
            return False
    return True