"""
QUESTION:
Write a function `next_prime(n)` that returns the smallest prime number larger than the given integer `n`. The function should have a time complexity of O(sqrt(n)) or better.
"""

import math

def next_prime(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    num = n + 1
    while not is_prime(num):
        num += 1
    return num