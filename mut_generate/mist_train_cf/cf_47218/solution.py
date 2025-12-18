"""
QUESTION:
Create a function called `int_to_binary` that takes a non-negative integer as input and returns its binary representation as a string. The function should not use built-in binary conversion functions, and the input integer is guaranteed to be a non-negative integer.
"""

def int_to_binary(n):
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary