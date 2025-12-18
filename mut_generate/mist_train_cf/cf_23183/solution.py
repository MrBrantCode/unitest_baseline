"""
QUESTION:
Write a function `replace_with_ascii` that takes a string of alphabetic characters as input, replaces each character with its corresponding ASCII code, removes any duplicates, reverses the resulting sequence, and returns the resulting string. The output string should consist of the ASCII codes represented as characters, not digits.
"""

def replace_with_ascii(s):
    ascii_codes = []
    for char in s:
        ascii_code = ord(char)
        if ascii_code not in ascii_codes:
            ascii_codes.append(ascii_code)
    
    ascii_codes.reverse()
    
    return ''.join(chr(code) for code in ascii_codes)