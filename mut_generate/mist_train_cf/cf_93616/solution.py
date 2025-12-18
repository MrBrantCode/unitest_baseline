"""
QUESTION:
Implement a function `binary_to_decimal(binary)` that takes a binary string as input and returns its corresponding decimal number without using any built-in functions or libraries for converting binary to decimal. The function should have a time complexity of O(n), where n is the length of the binary string.
"""

def binary_to_decimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    return decimal