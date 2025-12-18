"""
QUESTION:
Write a function named `replace_non_alphanumeric` that takes a string and a character as input, and returns the string with all non-alphanumeric characters replaced by the given character. The function should be efficient for strings of any length.
"""

def replace_non_alphanumeric(string, character):
    return ''.join(char if char.isalnum() else character for char in string)