"""
QUESTION:
Create a function `binary_to_decimal` that takes a binary number as input and returns its decimal equivalent. The function should not use built-in binary-to-decimal conversion functions, loops, or recursion.
"""

def binary_to_decimal(binary):
    binary_str = str(binary)
    decimal = 0
    for i in range(len(binary_str)):
        digit = int(binary_str[i])
        decimal += digit * (2 ** (len(binary_str) - i - 1))
    return decimal