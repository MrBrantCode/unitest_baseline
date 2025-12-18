"""
QUESTION:
Design a function `convert_to_hexadecimal` that takes a string as input, iterates through its numeric digits, and returns a list of hexadecimal representations of these digits. The function should exclude non-numeric characters from the input string and return the hexadecimal values as strings without the "0x" prefix.
"""

def convert_to_hexadecimal(string):
    """
    This function takes a string as input, iterates through its numeric digits, 
    and returns a list of hexadecimal representations of these digits.
    
    Args:
        string (str): The input string containing numeric digits.
    
    Returns:
        list: A list of hexadecimal representations of the numeric digits in the input string.
    """
    hex_list = []
    for char in string:
        if char.isdigit():
          hex_list.append(hex(int(char))[2:])
    return hex_list