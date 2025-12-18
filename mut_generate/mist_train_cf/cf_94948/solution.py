"""
QUESTION:
Write a function `binary_to_decimal(binary)` that converts a binary string into a decimal integer without using any built-in conversion functions or libraries, with a time complexity of O(n) and a space complexity of O(1), where n is the number of digits in the binary string.
"""

def binary_to_decimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal * 2
        if digit == '1':
            decimal = decimal + 1
    return decimal