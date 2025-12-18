"""
QUESTION:
Write a function called "swap_values" that takes two variables as arguments and swaps their integer values without using any arithmetic operators, temporary variables, or built-in swap functions. The function should return the updated values of the variables after the swap.
"""

def swap_values(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b