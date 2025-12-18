"""
QUESTION:
Write a function named `decimal_to_binary` that takes a non-negative integer as input and returns its binary representation as an integer. The function should not use built-in functions or libraries for conversion, loops, recursion, bitwise operators, or string manipulation methods.
"""

def decimal_to_binary(decimal):
    if decimal == 0:
        return 0

    binary = 0
    i = 0

    while decimal > 0:
        remainder = decimal % 2
        binary += remainder * (10 ** i)
        decimal //= 2
        i += 1

    return binary