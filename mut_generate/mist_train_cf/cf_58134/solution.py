"""
QUESTION:
Create a function `hex_to_binary(hex_string)` that takes a single hexadecimal character as a string and returns its binary representation as a string. If the input is not a valid hexadecimal character, return 'Error: Invalid hexadecimal input'. The binary representation should be padded with zeros to ensure its length is a multiple of 4.
"""

def hex_to_binary(hex_string):
    try:
        bin_string = bin(int(hex_string, 16))[2:]
        # Padding zeros if the binary string length is not multiple of 4
        if len(bin_string) % 4 != 0:
            bin_string = bin_string.zfill(4 * ((len(bin_string) // 4) + 1))
        return bin_string
    except ValueError:
        return 'Error: Invalid hexadecimal input'