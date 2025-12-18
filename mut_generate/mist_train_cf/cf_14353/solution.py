"""
QUESTION:
Write a Python function `convert_to_uppercase` that takes a string as input and returns the string with all lowercase letters converted to uppercase without using any built-in string methods or libraries.
"""

def convert_to_uppercase(input_string):
    """
    Converts all lowercase letters in the input string to uppercase without using any built-in string methods or libraries.

    Args:
        input_string (str): The input string to be converted.

    Returns:
        str: The input string with all lowercase letters converted to uppercase.
    """
    result = ""
    for char in input_string:
        ascii_value = ord(char)
        if 97 <= ascii_value <= 122:
            ascii_value -= 32
        result += chr(ascii_value)
    return result