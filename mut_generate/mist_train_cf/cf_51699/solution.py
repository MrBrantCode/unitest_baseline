"""
QUESTION:
Create a function `convert_special_chars_to_ascii(s)` that takes a string `s` as input and returns a string where all special characters in `s` are replaced with their corresponding ASCII values. A special character is defined as any character that is not a letter, digit, or space. The function should handle strings containing a mix of letters, digits, spaces, and special characters.
"""

def convert_special_chars_to_ascii(s):
    return ''.join([str(ord(c)) if not c.isdigit() and not c.isalpha() and not c.isspace() else c for c in s])