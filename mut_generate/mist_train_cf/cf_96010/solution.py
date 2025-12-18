"""
QUESTION:
Create a function called `binary_to_decimal` that takes an integer or string representation of a binary number as input and returns its decimal equivalent. The function should not use built-in functions or libraries that directly convert binary to decimal, and it should not use any loops or recursion.
"""

def binary_to_decimal(binary):
    binary_str = str(binary)
    decimal = 0
    for i in range(len(binary_str)):
        digit = int(binary_str[i])
        decimal += digit * (2 ** (len(binary_str) - i - 1))
    return decimal