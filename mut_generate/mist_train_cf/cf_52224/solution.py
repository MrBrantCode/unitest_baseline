"""
QUESTION:
Create a function named `get_signature()` that takes a user's input string and returns a string of binary ASCII values representing each character in the input string. The binary values should be 8 bits long and separated by spaces.
"""

def get_signature(input_string):
    """
    This function takes an input string and returns a string of binary ASCII values 
    representing each character in the input string. The binary values are 8 bits long 
    and separated by spaces.
    
    Parameters:
    input_string (str): The input string to be converted.
    
    Returns:
    str: A string of binary ASCII values.
    """
    ascii_signature = ''
    for letter in input_string:
        ascii_signature += format(ord(letter), '08b') + ' '
    return ascii_signature.strip()