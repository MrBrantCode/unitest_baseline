"""
QUESTION:
Write a Python function `string_convert(s)` that takes a string `s` as input and returns a dictionary containing its binary, hexadecimal, and octal representations. The input string should only consist of printable ASCII characters. If the input is invalid, return an error message. The binary representation should be in 8-bit format, and each character in the hexadecimal and octal representations should be separated by a colon.
"""

import string

def string_convert(s):
    if all(c in string.printable for c in s):
        binary = ' '.join(format(ord(i), '08b') for i in s)
        hexadecimal = ':'.join(hex(ord(x))[2:] for x in s) 
        octal = ':'.join(oct(ord(x))[2:] for x in s) 
        return {
            'Binary': binary,
            'Hexadecimal': hexadecimal,
            'Octal': octal
            }
    else:
        return "Error: Invalid input. Input string should only consist of printable ASCII characters."