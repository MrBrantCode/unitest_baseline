"""
QUESTION:
Write a function `smallest_divisible_number(n)` that takes a positive integer `n` and returns the smallest positive integer `m` such that the product of all the digits of `m` is divisible by `n`. If no such `m` exists, return -1.
"""

def smallest_divisible_number(n):
    if n == 1:
        return 1

    def product_of_digits(num):
        product = 1
        while num > 0:
            product *= num % 10
            num //= 10
        return product

    for m in range(1, 10**6):
        if product_of_digits(m) % n == 0:
            return m
    return -1