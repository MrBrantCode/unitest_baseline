"""
QUESTION:
Implement a function `add` that takes two integers `x` and `y` as inputs and returns their sum without using any arithmetic operators (+, -, *, /). The function should handle negative numbers correctly and only use bitwise operations and logical operations.
"""

def add(x, y):
    # Iterate until there is no carry
    while y != 0:
        # Carry contains common set bits of x and y
        carry = x & y

        # Sum of bits of x and y where at least one of the bits is not set
        x = x ^ y

        # Carry is shifted by one so that adding it to x gives the required sum
        y = carry << 1

    return x