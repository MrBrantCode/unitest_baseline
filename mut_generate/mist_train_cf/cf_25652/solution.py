"""
QUESTION:
Write a function `remove_non_alphabetic_chars` that takes a string as input and returns a new string containing only the alphabetic characters from the original string. The function should remove all non-alphabetic characters, including punctuation and special characters. The input string may contain any type of characters.
"""

def remove_non_alphabetic_chars(string):
    """
    This function takes a string as input and returns a new string containing only the alphabetic characters from the original string.

    Parameters:
    string (str): The input string

    Returns:
    str: A new string containing only the alphabetic characters from the original string
    """
    new_string = ""
    for char in string:
        if char.isalpha():
            new_string += char
    return new_string