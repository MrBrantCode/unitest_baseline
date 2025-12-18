"""
QUESTION:
Define a function `fib_sequence(n)` that calculates the number of even numbers (`X`), odd numbers (`Y`), and prime numbers (`Z`) in the first `n` elements of the Fibonacci sequence. Return `X`, `Y`, and `Z` modulo 2^20 as a tuple of three values.
"""

import math

mod = 2 ** 20

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = math.isqrt(n)
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def fib_sequence(n):
    x, y, z = 0, 0, 0
    a, b = 0, 1
    for i in range(n):
        if a % 2 == 0:
            x = (x + 1) % mod
        else:
            y = (y + 1) % mod
        if is_prime(a):
            z = (z + 1) % mod
        a, b = b, (a + b) % mod
    return x, y, z