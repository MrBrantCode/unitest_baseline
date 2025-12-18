"""
QUESTION:
Write a function called "swap_values" that takes two variables as arguments and swaps their values. The function should return the updated values of the variables after the swap. The implementation must not use any arithmetic operators or temporary variables.
"""

def swap_values(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b