"""
QUESTION:
Implement a function named `octal_to_bin` that takes an octal numeral as a string and returns its equivalent binary representation as a string. The input octal numeral is assumed to be valid.
"""

def octal_to_bin(octal_num):
    decimal = int(octal_num, 8)
    binary = bin(decimal).replace("0b", "")
    return binary