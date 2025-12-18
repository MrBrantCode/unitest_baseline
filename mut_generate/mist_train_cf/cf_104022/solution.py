"""
QUESTION:
Write a function named binary_to_decimal that takes a string of binary digits as input and returns its decimal equivalent. The function should not use the built-in int function.
"""

def binary_to_decimal(binary_str):
    decimal_num = 0
    for i, char in enumerate(binary_str[::-1]):
        decimal_num += int(char) * (2 ** i)
    return decimal_num