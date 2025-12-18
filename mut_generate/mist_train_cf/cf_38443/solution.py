"""
QUESTION:
Write a function `decode_hex_escape` that takes a string `hex_string` as input, where `hex_string` consists of hexadecimal escape sequences in the format `\xHH`, and returns the decoded ASCII representation as a string.

The input string `hex_string` is restricted to containing only hexadecimal escape sequences in the format `\xHH`, where `HH` represents a two-digit hexadecimal number. The function should return the corresponding ASCII characters decoded from the input hexadecimal escape sequences.
"""

def decode_hex_escape(hex_string: str) -> str:
    hex_list = hex_string.split("\\x")[1:]  
    decoded_string = ""
    for hex_val in hex_list:
        decoded_string += chr(int(hex_val, 16))  
    return decoded_string