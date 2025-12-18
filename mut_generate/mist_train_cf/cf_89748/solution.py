"""
QUESTION:
Design a function in Python, `check_all_primes`, to check if all numbers in a given list are prime. The function should take a list of integers as input and return a boolean value (True if all numbers are prime, False otherwise). The time complexity of the solution should be less than O(n^(1.5)), where n is the length of the input list.
"""

import math

def check_all_primes(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    for num in numbers:
        if not is_prime(num):
            return False
    return True