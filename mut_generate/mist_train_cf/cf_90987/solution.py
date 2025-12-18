"""
QUESTION:
Write a function named `convert_to_uppercase` that takes a string `s` as input and returns a new string in upper case. The function should not use any built-in functions or methods that directly convert a string to upper case. It should handle all types of characters, including special characters and non-alphabetic characters, without modifying the original string. The function should be case-sensitive and have a time complexity of O(n), where n is the length of the input string.
"""

def convert_to_uppercase(s):
    """
    Converts a string to uppercase without using built-in upper case conversion functions.

    Args:
        s (str): The input string.

    Returns:
        str: A new string in uppercase.
    """
    upper_s = ""
    for char in s:
        ascii_value = ord(char)
        if 97 <= ascii_value <= 122:  # lowercase letters range from 97 to 122 in ASCII
            upper_s += chr(ascii_value - 32)  # converting lowercase to uppercase by subtracting 32
        else:
            upper_s += char  # leaving non-alphabetic characters unchanged
    return upper_s