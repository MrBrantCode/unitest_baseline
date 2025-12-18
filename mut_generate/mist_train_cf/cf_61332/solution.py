"""
QUESTION:
Write a function `calculate_product` that takes a list of key-value pairs where keys are string representations of integers and values are strings, and returns the product of all unique keys converted to integers. The input list may contain duplicate keys, and the function should not skip any keys in the calculation.
"""

def calculate_product(lst):
    keys = list(set(k for k, v in lst))
    product = 1
    for key in keys:
        product *= int(key)
    return product