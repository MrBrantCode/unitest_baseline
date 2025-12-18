"""
QUESTION:
Design a function `product_of_digits(n)` that takes a positive integer `n` as input and returns the product of its individual digits.
"""

def product_of_digits(n):
    product = 1
    if n > 0:
        while n != 0:
            digit = n % 10
            product *= digit
            n = n // 10
    return product