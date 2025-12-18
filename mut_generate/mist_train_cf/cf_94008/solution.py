"""
QUESTION:
Create a function named "update_x" that takes an integer "x" as input and returns the value of "x" incremented by the nth prime number, where n is the value of "x" itself. The function should not take any additional parameters other than "x". The function should handle cases where "x" is a positive integer.
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

def update_x(x):
    nth_prime = get_nth_prime(x)
    return x + nth_prime