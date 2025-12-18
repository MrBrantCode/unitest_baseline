"""
QUESTION:
Write a function `check_strings` that takes a list of strings as input. The function should return `True` if any string in the list starts with "t", ends with "d", and has a length that is a prime number. Otherwise, it should return `False`.
"""

import math

def check_strings(lst):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    for word in lst:
        if word.startswith("t") and word.endswith("d") and is_prime(len(word)):
            return True
    return False