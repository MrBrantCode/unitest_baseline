"""
QUESTION:
Write a function `print_prime_numbers(a, b)` that prints all prime numbers within a given range from `a` to `b` (inclusive), where `a` and `b` are positive integers (1 ≤ a ≤ b ≤ 10^6). The function should have a time complexity of O(n log log n), where n is the maximum value between `a` and `b`, and a space complexity of O(1).
"""

import math

def entrance(a, b):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    for num in range(a, b + 1):
        if is_prime(num):
            print(num)