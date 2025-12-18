"""
QUESTION:
Write a function `compute_absolute_product(lst)` that takes a list of numbers as input, computes the product of their absolute values after rounding down to the nearest integer, excluding prime numbers. Consider only positive integers as prime numbers. The function should return the product as an integer.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def compute_absolute_product(lst):
    product = 1
    for num in lst:
        num = int(abs(num))
        if not is_prime(num):
            product *= num
    return product