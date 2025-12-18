"""
QUESTION:
Write a function `prime_product` that takes a list of integers as input and returns the product of all prime numbers in the list.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_product(lst):
    product = 1
    for num in lst:
        if is_prime(num):
            product *= num
    return product