"""
QUESTION:
Implement a function called `elementwise_product` that takes two lists of integers `a` and `b` as input and returns a list of integers representing the element-wise product of `a` and `b`. The input lists are of equal length `n` (1 ≤ n ≤ 1000), may contain negative integers, duplicate elements, or floating-point numbers (which should be rounded to the nearest integer for the output), and may be empty (n = 0). The implementation should have a time complexity of O(n) or better.
"""

def elementwise_product(a, b):
    if len(a) != len(b):
        return "Error: The input lists must have the same length"
    
    product = []
    for i in range(len(a)):
        product.append(round(a[i] * b[i]))
    
    return product