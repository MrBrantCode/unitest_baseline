"""
QUESTION:
Write a function `to_hexadecimal(s)` that takes a string of alphanumeric characters and returns its corresponding hexadecimal representation. The function should work for both numeric and non-numeric characters in the string. If the string contains non-numeric characters, convert each character into its hexadecimal ASCII value.
"""

def to_hexadecimal(s):
    return ''.join([hex(ord(c))[2:] for c in s])