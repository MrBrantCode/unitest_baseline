"""
QUESTION:
Create a function `replace_unicode_str` that replaces all non-alphanumeric and non-ASCII characters from an input string with their hexadecimal Unicode representation. The function should take a string as input and return the modified string, where each non-alphanumeric and non-ASCII character is replaced by its 4-digit hexadecimal Unicode code point with leading zeroes if necessary.
"""

def replace_unicode_str(input_str):
    return ''.join([ch if ch.isalnum() and ord(ch) < 128 else '\\u{0:04x}'.format(ord(ch)) for ch in input_str])