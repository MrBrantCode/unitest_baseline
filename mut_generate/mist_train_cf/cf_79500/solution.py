"""
QUESTION:
Write a function named `calculate_product` that takes a dictionary as input where keys are strings representing decimal numbers. The function should calculate the product of all unique dictionary keys after converting them to integers. The function should maintain optimal time complexity and handle dynamic dictionary sizes.
"""

from functools import reduce
import operator

def calculate_product(dic):
    # Remove duplicates and convert keys to integer
    keys = set(int(float(key)) for key in dic)

    # Multiply all keys together
    product = reduce(operator.mul, keys, 1)

    return product