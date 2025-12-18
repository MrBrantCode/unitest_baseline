"""
QUESTION:
Create a program with two functions, `encode_ascii_to_hex(char)` and `decode_hex_to_ascii(hex_val)`, that can convert a printable ASCII character to its hexadecimal value and back to the original character. The functions should maintain the integrity of the original character after multiple transformations. The input for `encode_ascii_to_hex` is a single printable ASCII character and the output should be its hexadecimal value. The input for `decode_hex_to_ascii` is a hexadecimal value and the output should be the corresponding ASCII character.
"""

def encode_ascii_to_hex(char):
    return hex(ord(char))

def decode_hex_to_ascii(hex_val):
    return chr(int(hex_val, 16))