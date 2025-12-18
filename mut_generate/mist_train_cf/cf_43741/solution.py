"""
QUESTION:
Write a program that contains two functions: `hex_to_ascii(hex_values)` and `ascii_to_hex(ascii_values)`. `hex_to_ascii(hex_values)` takes a list of hexadecimal values of uppercase letters as input, converts them to their corresponding ASCII characters, and returns the result as a string. `ascii_to_hex(ascii_values)` takes a string of uppercase ASCII characters as input, converts them to the hexadecimal values of their corresponding uppercase letters, and returns the result as a string of space-separated hexadecimal values. The program should handle invalid inputs appropriately.
"""

def hex_to_ascii(hex_values):
    return ''.join(chr(int(hex_value, 16)) for hex_value in hex_values)

def ascii_to_hex(ascii_values):
    return ' '.join(hex(ord(char)).split('x')[-1] for char in ascii_values)