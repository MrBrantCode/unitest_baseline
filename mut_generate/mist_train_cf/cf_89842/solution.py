"""
QUESTION:
Write a function `swap_variables` that takes two integers `a` and `b` and swaps their values using only bitwise operators and without using any arithmetic or assignment operators, conditional statements, or loops.
"""

def swap_variables(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b