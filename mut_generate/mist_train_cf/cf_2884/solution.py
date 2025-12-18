"""
QUESTION:
Write a function `find_next_prime(n)` that takes an integer `n` as input and returns the smallest prime number larger than `n`. The function should have a time complexity of O(log(n)) or better. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def find_next_prime(n):
    next_num = n + 1
    while True:
        if is_prime(next_num):
            return next_num
        next_num += 1