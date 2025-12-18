"""
QUESTION:
Write a function `binary_to_decimal` that takes a binary string as input and returns its decimal equivalent without using built-in conversion functions or libraries. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of digits in the binary string. The binary string can have up to 1 billion digits.
"""

def binary_to_decimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal * 2
        if digit == '1':
            decimal = decimal + 1
    return decimal