"""
QUESTION:
Write a function called `get_prime_numbers` that takes a list of integers and returns a new list containing only the prime numbers from the original list. The function should have a time complexity of O(n*sqrt(m)), where n is the length of the original list and m is the maximum value in the original list.
"""

import math

def get_prime_numbers(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    return [num for num in lst if is_prime(num)]