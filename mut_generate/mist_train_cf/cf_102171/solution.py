"""
QUESTION:
Write a function named `find_product` that takes a dictionary as input, calculates the product of its values that are divisible by 3 and less than 100, and returns the result. If no values meet these conditions, return -1.
"""

def find_product(d):
    product = 1
    for key, value in d.items():
        if value % 3 == 0 and value < 100:
            product *= value
    if product == 1:
        return -1
    return product