"""
QUESTION:
Write a function `multiply_abs_values_v2(lst)` that takes a list of numerical values, returns the product of the absolute integer parts of the numbers excluding those divisible by 2, 3, or 5, and rounds down the absolute values to the nearest integer before checking for divisibility and calculating the product.
"""

import math

def multiply_abs_values_v2(lst):
    primes = [2, 3, 5]
    values = [math.floor(abs(n)) for n in lst if all(math.floor(abs(n)) % p != 0 for p in primes)]
    return math.prod(values)