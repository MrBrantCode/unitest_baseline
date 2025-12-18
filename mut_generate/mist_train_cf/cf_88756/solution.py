"""
QUESTION:
Write a function called `fibonacci_prime_square` that takes an integer `n` as input and prints out the Fibonacci series up to `n`. The Fibonacci number should only be printed if it is both prime and a perfect square. The input `n` is guaranteed to be greater than 1.
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

def fibonacci_prime_square(n):
    a, b = 0, 1
    while b <= n:
        if is_prime(b) and is_perfect_square(b):
            print(b)
        a, b = b, a + b