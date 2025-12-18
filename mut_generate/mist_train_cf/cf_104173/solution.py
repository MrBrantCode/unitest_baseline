"""
QUESTION:
Create a function `convert_to_hex(string)` that takes a string of lowercase letters (maximum 1000 characters) as input and returns its hexadecimal representation as a string. The function should handle empty strings and use an iterative approach.
"""

def convert_to_hex(string):
    if not string:
        return ''
    
    hex_code = ''
    for char in string:
        hex_code += format(ord(char), 'x')
    
    return hex_code