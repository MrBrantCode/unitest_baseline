"""
QUESTION:
Write a function `greatest_prime(n)` that determines the greatest prime divisor of a given integer `n`. The function should return the largest prime factor of `n`. The input `n` can be a large number, so the function should be efficient and handle cases where `n` is a prime number itself.
"""

import math

def greatest_prime(n):
    def is_prime(num):
        for i in range(2, math.isqrt(num) + 1):
            if num % i == 0:
                return False
        return True

    def next_prime(num):
        prime = num + 1
        while not is_prime(prime):
            prime += 1
        return prime

    factor = 2
    while factor * factor <= n:
        while n % factor == 0:
            n //= factor
        factor = next_prime(factor)

    return n