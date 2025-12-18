"""
QUESTION:
Design a function `generate_fibonacci_primes(y)` that generates a Fibonacci sequence up to the given number `y` and identifies whether each generated Fibonacci number is a prime number or not. The function should have a time complexity of O(n*sqrt(n)) or better.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_fibonacci_primes(y):
    a, b = 0, 1
    while a <= y:
        if is_prime(a):
            print(f"{a} is a prime number")
        else:
            print(f"{a} is not a prime number")
        a, b = b, a + b