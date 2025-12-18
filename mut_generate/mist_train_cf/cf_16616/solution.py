"""
QUESTION:
Replace all spaces in a string with a given character and count the number of replacements made, but do not use any built-in string methods.

Implement a function `replace_and_count` that takes two parameters: a string `s` and a character `c`. It should replace all spaces in the string with the given character and return the modified string along with the number of replacements made.
"""

def replace_and_count(s, c):
    """
    Replaces all spaces in a string with a given character and counts the number of replacements made.

    Parameters:
    s (str): The input string.
    c (str): The character to replace spaces with.

    Returns:
    tuple: A tuple containing the modified string and the number of replacements made.
    """
    modified_string = ""
    replacement_count = 0
    for char in s:
        if char == ' ':
            modified_string += c
            replacement_count += 1
        else:
            modified_string += char
    return modified_string, replacement_count