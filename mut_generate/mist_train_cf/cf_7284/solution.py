"""
QUESTION:
Implement a function named `swap_variables` that takes two integers `a` and `b` as input and swaps their values without using any arithmetic or assignment operators, conditional statements, or loops, but only bitwise operators.
"""

def swap_variables(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b