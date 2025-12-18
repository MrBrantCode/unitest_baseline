"""
QUESTION:
Create a function `ascii_code_converter` that takes a string as input and returns a list of ASCII codes corresponding to each character in the string. The function should work with strings containing single words and multiple words.
"""

def ascii_code_converter(input_string):
    """
    This function takes a string as input and returns a list of ASCII codes 
    corresponding to each character in the string.

    Args:
    input_string (str): The input string to be converted into ASCII codes.

    Returns:
    list: A list of ASCII codes corresponding to each character in the input string.
    """
    return [ord(c) for c in input_string]