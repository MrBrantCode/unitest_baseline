"""
QUESTION:
Create a function named `to_hex` that takes an alphanumeric string as input and returns its corresponding hexadecimal representation. The function should work by converting each character to its corresponding Unicode code point and then to hexadecimal, removing the '0x' prefix, and joining all the hex values into a single string. The function should assume Python 3 and not handle any potential errors.
"""

def to_hex(s):
    return ''.join(hex(ord(c))[2:] for c in s)