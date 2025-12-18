"""
QUESTION:
Write a function `string_to_binary` that takes a string `s` as input and returns its binary representation, where each character is converted to its binary equivalent using its Unicode code point and the resulting binary strings are separated by a space. The binary strings should be padded with zeros on the left to a minimum length of 8 bits.
"""

def string_to_binary(s):
    return ' '.join(format(ord(c), '08b') for c in s)