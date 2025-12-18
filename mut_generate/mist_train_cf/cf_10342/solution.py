"""
QUESTION:
Write a Python function called "swap_values" that takes two variables as arguments and swaps their values in-place without using any built-in functions or temporary variables. The function should return the updated values of the variables after the swap.
"""

def entrance(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b