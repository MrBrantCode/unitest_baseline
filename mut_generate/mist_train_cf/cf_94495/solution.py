"""
QUESTION:
Write a Python function called "swap_values" that takes two variables as arguments and swaps their values without using arithmetic operators or temporary variables. The function should return the updated values of the variables after the swap.
"""

def swap_values(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b