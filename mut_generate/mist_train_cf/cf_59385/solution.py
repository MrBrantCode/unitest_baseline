"""
QUESTION:
Create a function `int_to_binary(n)` that takes a non-negative integer `n` as input and returns its binary representation as a string without using built-in or library functions for binary conversion. The function should handle the case where `n` is 0.
"""

def int_to_binary(n):
    binary = ""

    if n == 0:
        return "0"

    while n > 0:
        binary = str(n%2) + binary
        n = n // 2

    return binary