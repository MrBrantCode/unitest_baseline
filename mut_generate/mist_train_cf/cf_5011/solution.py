"""
QUESTION:
Write a function `to_hexadecimal(s)` that takes a string `s` of up to 100 characters as input and returns its hexadecimal representation as a string with lowercase characters. The function should ignore non-alphanumeric characters, handle both uppercase and lowercase letters, convert special characters to their corresponding ASCII values in hexadecimal representation, and handle negative numbers by converting them to their two's complement hexadecimal representation.
"""

def to_hexadecimal(s):
    hex_list = []
    
    for c in s:
        if not c.isalnum():
            continue
        
        if c.startswith('-'):
            hex_value = hex(int(c, 10) & 0xFFFFFFFFFFFFFFFF)[2:]
        else:
            hex_value = hex(ord(c))[2:]
        
        hex_list.append(hex_value.lower())
    
    return ''.join(hex_list)