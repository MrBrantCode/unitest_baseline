"""
QUESTION:
Write a function `binary_to_decimal(binary)` that takes a binary string as input and returns its decimal equivalent. The input string consists only of '0' and '1' characters. The function should handle binary strings of any length.
"""

def binary_to_decimal(binary):
    decimal = 0
    power = len(binary) - 1
    for digit in binary:
        if digit == '1':
            decimal += 2 ** power
        power -= 1
    return decimal