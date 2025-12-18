"""
QUESTION:
Write a function `increment_by_nth_prime` that takes an integer `x` and increments its value by the nth prime number, where n is the value of `x` itself. The function should return the updated value of `x`.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def get_nth_prime(n):
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            count += 1
        num += 1
    return num - 1

def increment_by_nth_prime(x):
    return x + get_nth_prime(x)