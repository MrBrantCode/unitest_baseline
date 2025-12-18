"""
QUESTION:
Create a function `convert_to_uppercase(string)` that takes a string as input, converts all lowercase letters to uppercase, removes any whitespace characters, and returns the converted string along with the count of unique uppercase characters in the string. Do not use any built-in string methods or libraries for case conversion. The function should handle special characters, punctuation marks, and symbols, retaining their original positions in the string.
"""

def convert_to_uppercase(string):
    """
    This function takes a string as input, converts all lowercase letters to uppercase, 
    removes any whitespace characters, and returns the converted string along with 
    the count of unique uppercase characters in the string.

    Args:
        string (str): The input string to be converted.

    Returns:
        tuple: A tuple containing the converted string and the count of unique uppercase characters.
    """
    uppercase_chars = set()
    converted_string = ""

    for char in string:
        if char != " ":
            uppercase_char = chr(ord(char) - 32) if ord(char) >= 97 and ord(char) <= 122 else char
            converted_string += uppercase_char
            if 'A' <= char <= 'Z' or 'A' <= uppercase_char <= 'Z':
                uppercase_chars.add(uppercase_char)

    return converted_string, len(uppercase_chars)