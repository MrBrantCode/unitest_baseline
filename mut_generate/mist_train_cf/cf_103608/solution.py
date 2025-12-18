"""
QUESTION:
Write a function `next_prime` that takes an integer `number` as input and returns the smallest prime number greater than the given number. The function should also determine whether the given number is a prime number. Assume the input number is a positive integer.
"""

import math

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

def next_prime(number):
    next_num = number + 1
    while True:
        if is_prime(next_num):
            return next_num
        next_num += 1