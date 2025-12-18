"""
QUESTION:
Create a function called `str_to_binary` that takes a string as input and returns its binary representation. The binary representation of each character in the string should be 8 bits long, padded with zeros if necessary. The function should return the binary representation of the entire string as a single string of binary digits.
"""

def str_to_binary(s):
    binary = ''
    for c in s:
        binary += format(ord(c), '08b')
    return binary