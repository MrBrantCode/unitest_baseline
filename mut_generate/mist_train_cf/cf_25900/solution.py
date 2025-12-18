"""
QUESTION:
Create a function called `hex_to_bin` that takes a string representing a hexadecimal number as input and returns its binary representation as a string. The function should return "Invalid Hexadecimal!!" if the input string is not a valid hexadecimal number.
"""

def hex_to_bin(hex_str):
    try:
        return bin(int(hex_str, 16))[2:]
    except ValueError:
        return "Invalid Hexadecimal!!"