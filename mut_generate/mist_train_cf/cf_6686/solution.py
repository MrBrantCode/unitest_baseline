"""
QUESTION:
Write a function `swap_values(a, b)` that swaps the values of two variables 'a' and 'b' without using a temporary variable, the +, -, *, / operators, or any bitwise operators.
"""

def swap_values(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b