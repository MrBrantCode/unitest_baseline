"""
QUESTION:
Create a function named `hex_to_bin` that takes a string of hexadecimal digits as input and returns its corresponding binary representation as a string. The function should handle both single and multi-digit hexadecimal numbers. If the input string is not a valid hexadecimal number, the function should return the error message "Error: Invalid hexadecimal number."
"""

def hex_to_bin(hex_str):
    try:
        int(hex_str, 16)
    except ValueError:
        return "Error: Invalid hexadecimal number."
    
    bin_str = bin(int(hex_str, 16))[2:]  # strip off the '0b' prefix returned by bin function
    return bin_str