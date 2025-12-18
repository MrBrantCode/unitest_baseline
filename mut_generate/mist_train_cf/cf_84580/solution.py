"""
QUESTION:
Create a function `swap_xor` that takes two integers as input and swaps their values using bitwise XOR operations without using a temporary variable. The function should return the swapped values.
"""

def swap_xor(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b