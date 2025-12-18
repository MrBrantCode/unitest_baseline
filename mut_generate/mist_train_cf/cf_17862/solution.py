"""
QUESTION:
Write a function `decimal_to_hexadecimal` that takes a string of binary digits as input, converts it to a hexadecimal number, and returns the result as a string in uppercase. The input binary number is guaranteed to be valid.
"""

def decimal_to_hexadecimal(binary_str):
    decimal = int(binary_str, 2)
    return format(decimal, 'X')