"""
QUESTION:
Create a function called binary_to_hex that takes a string of binary characters as input and returns its equivalent hexadecimal value. The input string consists of '0's and '1's, and the output should be in lowercase hexadecimal format without the '0x' prefix.
"""

def binary_to_hex(binary_string):
    # convert binary string to decimal
    decimal = int(binary_string, 2)
    
    # convert decimal to hexadecimal
    hexadecimal = hex(decimal)
    
    # remove '0x' prefix from hexadecimal string and convert to lowercase
    hexadecimal = hexadecimal[2:].lower()
    
    return hexadecimal