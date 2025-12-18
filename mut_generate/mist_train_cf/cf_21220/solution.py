"""
QUESTION:
Create a function `f(n)` that prints all prime numbers less than `n` that are divisible by both 5 and 7. Note that a prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def f(n):
    i = 0
    while i < n:
        i += 1
        if i % 5 == 0 and i % 7 == 0 and is_prime(i):
            print(i)