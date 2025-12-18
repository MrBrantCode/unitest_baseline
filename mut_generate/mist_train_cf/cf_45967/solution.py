"""
QUESTION:
Write a function called `hex_to_ascii` that takes a string of hexadecimal values as input, where each pair of hexadecimal values represents an ASCII character. The function should convert these hexadecimal values to their corresponding ASCII characters, validate the input to ensure only valid ASCII characters are represented, and return the resulting string of ASCII characters. If any invalid ASCII character is found, return the error message "Invalid input: Non-ASCII character found." The function should be able to handle input strings of varying lengths.
"""

def hex_to_ascii(hex_string):
    output = ""
    hex_chars = [hex_string[i:i+2] for i in range(0, len(hex_string), 2)]
    
    for hex_char in hex_chars:
        ascii_char = chr(int(hex_char, 16))
        if ascii_char.isascii():
            output += ascii_char
        else:
            return "Invalid input: Non-ASCII character found."
    return output