"""
QUESTION:
Write a function `swap_values(a, b, c)` that swaps the values of three variables `a`, `b`, and `c` without using any additional variables.
"""

def swap_values(a, b, c):
    a = a + b + c
    b = a - (b + c)
    c = a - (b + c)
    a = a - (b + c)
    return a, b, c