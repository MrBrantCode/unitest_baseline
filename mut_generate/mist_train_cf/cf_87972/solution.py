"""
QUESTION:
Write a function called `swap_values` that takes three variables `a`, `b`, and `c` as input, swaps their values without using any additional variables, and returns the swapped values. The function must have a time complexity of O(1).
"""

def swap_values(a, b, c):
    a = a ^ b ^ c
    b = a ^ b ^ c
    c = a ^ b ^ c
    a = a ^ b ^ c
    return a, b, c