"""
QUESTION:
Write a function named `increment_by_next_prime` that takes an integer `x` and increments its value by the next prime number after `x`. The function should return the updated value of `x`. Assume `x` is an integer greater than 1.
"""

import math

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

def increment_by_next_prime(x):
    next_prime = x
    while True:
        next_prime += 1
        if is_prime(next_prime):
            return x + next_prime