"""
QUESTION:
Write a function `product_of_elements` that calculates the product of the first 100 elements in the series of natural numbers after passing them through a quadratic function f(x) = ax^2 + bx + c, where a, b, and c are integers.
"""

def product_of_elements(a, b, c):
    product = 1
    for x in range(1, 101):
        y = a*x**2 + b*x + c
        product *= y
    return product