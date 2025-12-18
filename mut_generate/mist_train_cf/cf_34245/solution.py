"""
QUESTION:
Write a function `decode_hex_string` that takes a string of hexadecimal escape sequences as input and returns the decoded ASCII string. The input string consists of a series of hexadecimal escape sequences, each representing a character in the string. Function signature: `def decode_hex_string(hex_string: str) -> str`
"""

def decode_hex_string(hex_string: str) -> str:
    decoded_string = ""
    hex_list = hex_string.split("\\x")[1:]  
    for hex_char in hex_list:
        decoded_string += chr(int(hex_char, 16))  
    return decoded_string