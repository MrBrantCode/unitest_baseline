"""
QUESTION:
Write a function `swap_numbers` that swaps two numbers `a` and `b` without using arithmetic or assignment operators, conditional statements, or loops.
"""

def swap_numbers(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b