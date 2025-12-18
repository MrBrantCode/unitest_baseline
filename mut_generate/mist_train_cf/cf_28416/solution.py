"""
QUESTION:
Write a function `replace_letters` that takes a string `s` as input and returns a new string where all lowercase letters in `s` are replaced with their corresponding uppercase letters. The function should not use the `replace` method.
"""

def replace_letters(s: str) -> str:
    modified_string = ""
    for char in s:
        if 'a' <= char <= 'z':
            modified_string += chr(ord(char) - 32)  # Convert lowercase to uppercase using ASCII values
        else:
            modified_string += char
    return modified_string