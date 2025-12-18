"""
QUESTION:
Create a function named `copy_unique_string` that takes a string as input and returns a new string containing the first occurrence of each character in the original string. The function should exclude any duplicate characters found later in the string.
"""

def copy_unique_string(string):
    """
    Returns a new string containing the first occurrence of each character in the original string.
    
    Args:
    string (str): The input string.
    
    Returns:
    str: A new string with unique characters.
    """
    unique_string = ""
    unique_chars = []
    for char in string:
        if char not in unique_chars:
            unique_chars.append(char)
            unique_string += char
    return unique_string