"""
QUESTION:
Write a function `binary_to_decimal(binary_string)` that takes a string of binary digits ('0's and '1's) and returns the corresponding decimal number. The function should work for any string of binary digits.
"""

def binary_to_decimal(binary_string):
    decimal = 0
    for i in range(len(binary_string)):
        decimal += int(binary_string[-i - 1]) * 2 ** i
    return decimal