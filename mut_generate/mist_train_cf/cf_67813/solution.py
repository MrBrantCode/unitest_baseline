"""
QUESTION:
Write a function named `product` that calculates the product of all prime numbers and perfect square numbers within a given sequence. The sequence is a list of integers and may contain any positive or non-positive integers. The function should return the product as an integer.
"""

import math

def product(sequence):
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

    def is_perfect_square(n):
        if n < 1:
            return False
        root = math.isqrt(n)
        return n == root * root

    product = 1
    for num in sequence:
        if is_prime(num) or is_perfect_square(num):
            product *= num
    return product