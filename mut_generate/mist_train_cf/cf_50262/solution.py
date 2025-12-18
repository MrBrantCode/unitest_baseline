"""
QUESTION:
Create a function named `text_to_hex` that takes a string as input and returns a string of hexadecimal codes, each representing the ASCII value of the corresponding character in the input string. The output should not include the '0x' prefix that typically indicates hexadecimal numbers in Python.
"""

def text_to_hex(text):
    return ''.join([hex(ord(c)).split('x')[-1] for c in text])