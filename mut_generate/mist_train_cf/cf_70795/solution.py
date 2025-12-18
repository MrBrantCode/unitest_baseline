"""
QUESTION:
Develop a function called `hex_to_utf8` that takes a list of hexadecimal strings as input, converts each hexadecimal string into its corresponding UTF-8 character(s), and returns a list of these UTF-8 characters. The function should support both single and multi-byte UTF-8 characters.
"""

def hex_to_utf8(hex_values):
    utf8_chars = []
    for hex_value in hex_values:
        bytes_object = bytes.fromhex(hex_value)
        utf8_string = bytes_object.decode("utf-8")
        utf8_chars.append(utf8_string)
    return utf8_chars