"""
QUESTION:
Write a function `print_fibonacci` that prints the Fibonacci numbers up to a given number `n`, but only if the number is both prime and a perfect square, and `n` must be greater than 1.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect_square(n):
    root = int(math.sqrt(n))
    return root * root == n

def print_fibonacci(n):
    a, b = 0, 1
    while b <= n:
        if is_prime(b) and is_perfect_square(b):
            print(b)
        a, b = b, a + b