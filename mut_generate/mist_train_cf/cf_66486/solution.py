"""
QUESTION:
Create a function `hex_to_ascii` that takes a string of hexadecimal characters as input and returns its corresponding ASCII representation. The function should interpret the input string in pairs of hexadecimal digits, converting each pair to its corresponding ASCII character.
"""

def hex_to_ascii(hex_str):
    """
    This function takes a string of hexadecimal characters as input and returns its corresponding ASCII representation.
    
    Parameters:
    hex_str (str): A string of hexadecimal characters.
    
    Returns:
    str: The ASCII representation of the input hexadecimal string.
    """
    ascii_str = ""
    for i in range(0, len(hex_str), 2):
        part = hex_str[i : i + 2]
        ch = chr(int(part, 16))
        ascii_str += ch
    return ascii_str