"""
QUESTION:
Write a function `binary_to_octal(binary_num)` that converts a binary number to its corresponding octal numeral. The function should take a string `binary_num` representing a binary number as input and return the equivalent octal numeral as a string. The octal numeral should not include the "0o" prefix.
"""

def binary_to_octal(binary_num):
    decimal = int(binary_num, 2)
    return oct(decimal)[2:]