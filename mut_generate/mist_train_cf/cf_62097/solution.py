"""
QUESTION:
Write a function `triple_product(x, y)` that takes two positive integers `x` and `y` as input and returns the product of `x`, `y`, and the reversed digits of their product. The reversed digits are obtained by converting the product to a string, reversing it, and converting it back to an integer. Assume the product of `x` and `y` is a single or two-digit number.
"""

def triple_product(x, y):
    product = x * y
    reversed_product = int(str(product)[::-1])
    return product * reversed_product