"""
QUESTION:
Write a function named `to_hexadecimal` that takes a string `s` of length up to 100 characters as input and returns its hexadecimal representation as a string. The function should ignore non-alphanumeric characters, handle both uppercase and lowercase letters, convert special characters to their corresponding ASCII values in hexadecimal representation, and convert negative numbers to their two's complement hexadecimal representation. The output should be a string with lowercase hexadecimal characters.
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