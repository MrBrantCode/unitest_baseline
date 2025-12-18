"""
QUESTION:
Create a function named `multiply(a, b)` that calculates the product of two integers `a` and `b` without directly using the multiplication operator. The function should handle both positive and negative integers, and return the correct product.
"""

def multiply(a, b):
    product = 0
    for i in range(abs(b)):
        product += a
    if b < 0:
        product = -product
    return product