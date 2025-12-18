"""
QUESTION:
Write a function called `string_to_binary` that takes a string `text` as input and returns the binary equivalent of the input string. The binary equivalent should be a string of binary digits separated by spaces, where each binary digit is an 8-bit binary representation of the ASCII value of a character in the input string. The function should not take any additional parameters other than the input string.
"""

def string_to_binary(text):
    binary = ' '.join(format(ord(char), '08b') for char in text)
    return binary