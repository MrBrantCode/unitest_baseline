"""
QUESTION:
Create a function `get_next_prime` that increments a given number `x` by the next prime number after 3. Assume `x` is 3.
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

def get_next_prime(x):
    while True:
        x += 1
        if is_prime(x):
            return x