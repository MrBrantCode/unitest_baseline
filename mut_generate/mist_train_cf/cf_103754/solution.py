"""
QUESTION:
Write a function `decimal_to_binary` that takes a string input representing a decimal number and returns its binary representation as a string. The function should handle cases where the input is not a valid number, and return `None` in such cases. The binary representation should be returned without the '0b' prefix.
"""

def decimal_to_binary(number):
    try:
        decimal = int(number)
        binary = bin(decimal)[2:]
        return binary
    except ValueError:
        return None