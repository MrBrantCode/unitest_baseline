"""
QUESTION:
Design a function `hex_to_text` that takes a string of hexadecimal digits as input and returns the corresponding text string. The input string may contain ASCII-encoded characters and should be decoded accordingly. The function should support UTF-8 encoding.
"""

def hex_to_text(hexadecimal):
    hex_str = bytes.fromhex(hexadecimal).decode('utf-8') 
    return hex_str