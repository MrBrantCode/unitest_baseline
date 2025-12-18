"""
QUESTION:
Write a function named `convert_to_uppercase` that takes a string `s` as input and returns a new string where all lowercase letters in `s` are converted to uppercase, without using any built-in functions or methods that directly convert a string to upper case. The function should have a time complexity of O(n), where n is the length of the input string, and should handle all types of characters, including special characters and non-alphabetic characters, leaving them unchanged.
"""

def convert_to_uppercase(s):
    """
    This function takes a string `s` as input and returns a new string 
    where all lowercase letters in `s` are converted to uppercase, 
    without using any built-in functions or methods that directly 
    convert a string to upper case.

    Time complexity: O(n), where n is the length of the input string.

    Parameters:
    s (str): The input string.

    Returns:
    str: The string with all lowercase letters converted to uppercase.
    """
    upper_s = ""
    for char in s:
        ascii_value = ord(char)
        if 97 <= ascii_value <= 122:  # lowercase letters range from 97 to 122 in ASCII
            upper_s += chr(ascii_value - 32)  # converting lowercase to uppercase by subtracting 32
        else:
            upper_s += char  # leaving non-alphabetic characters unchanged
    return upper_s