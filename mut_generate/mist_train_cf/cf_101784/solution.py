"""
QUESTION:
Write a function `calculate_difference` that takes three integers `a`, `b`, and `c` as input. The function should calculate the sum of `a`, `b`, and `c`, then find the difference between the product of the sum and the quotient of `b` and `a`, and the product of the sum and the quotient of 5436 and `c`. The function should return the values of `a`, `b`, `c`, the sum, the two products, and the difference.
"""

def calculate_difference(a, b, c):
    sum_abc = a + b + c
    product1 = sum_abc * (b / a)
    product2 = sum_abc * (5436 / c)
    diff = product1 - product2
    return a, b, c, sum_abc, product1, product2, diff