"""
QUESTION:
Write a function named `swap` that swaps the values of two variables using bitwise operators without utilizing an extra buffer variable. The function should take two arguments, `a` and `b`.
"""

def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b