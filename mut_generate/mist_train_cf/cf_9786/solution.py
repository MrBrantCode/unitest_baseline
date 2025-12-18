"""
QUESTION:
Create a function `convert_to_hex(string)` that takes a string consisting of only lowercase letters (up to 100 characters) as input and returns its hexadecimal code representation. The function should also handle empty strings.
"""

def convert_to_hex(string):
    # Handle empty strings
    if len(string) == 0:
        return ""
    
    # Convert each character to hexadecimal code and join them
    hex_code = "".join([hex(ord(c))[2:] for c in string])
    
    return hex_code