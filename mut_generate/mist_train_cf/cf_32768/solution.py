"""
QUESTION:
Create a function `add_binary` that takes two non-negative integers `a` and `b` as input and returns their sum in binary form as a string.
"""

def add_binary(a, b):
    return bin(a + b)[2:]