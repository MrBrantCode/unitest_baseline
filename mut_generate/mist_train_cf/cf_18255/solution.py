"""
QUESTION:
Write a function called `swap_values` that takes three arguments `a`, `b`, and `c`. The function should swap the values of `a`, `b`, and `c` in a cyclical manner (i.e., the value of `a` moves to `b`, the value of `b` moves to `c`, and the value of `c` moves to `a`) without using any additional variables. The function should return the swapped values of `a`, `b`, and `c`.
"""

def swap_values(a, b, c):
    a = a + b + c
    b = a - (b + c)
    c = a - (b + c)
    a = a - (b + c)
    return a, b, c