"""
QUESTION:
Implement two functions: `str_to_hex` and `hex_to_str`. The `str_to_hex` function should take a string as input, convert each character into its hexadecimal ASCII representation, and return the concatenated hexadecimal values as a string. The `hex_to_str` function should take the hexadecimal string as input, convert each hexadecimal value back to its original ASCII character, and return the original string. The implementation should not use built-in encoding or decoding functions, and it should consider the standard ASCII representation of characters.
"""

def str_to_hex(input_string):
    hex_output = ""
    for character in input_string:
        ascii_val = ord(character)  # Get the ASCII value of the character
        hex_val = hex(ascii_val)[2:]  # Convert to hex, strip '0x'
        hex_output += hex_val + " "  # Concatenate to output string
    return hex_output.rstrip()  # Return the hexadecimal representation

def hex_to_str(input_hex):
    str_output = ""
    hex_values = input_hex.split()
    for hex_val in hex_values:
        ascii_val = int(hex_val, 16)  # Convert hex back to integer ASCII value
        str_output += chr(ascii_val)  # Convert ASCII value back to character
    return str_output  # Return the original string