"""
QUESTION:
Write a function `convert_hex(hex_value)` that takes a string representing a hexadecimal value as input and returns its equivalent binary and decimal values. The input hexadecimal value should be a string, and it may or may not have the "0x" prefix. The output binary value should be a string of binary digits without the "0b" prefix, and the output decimal value should be an integer.
"""

def convert_hex(hex_value):
    # convert hexadecimal to decimal
    decimal_value = int(hex_value, 16)
    
    # convert decimal to binary
    binary_value = bin(decimal_value).replace("0b", "")
    
    return binary_value, decimal_value