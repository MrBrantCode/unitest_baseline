"""
QUESTION:
Write a function named `convert_to_uppercase` that takes a string as input and returns the string with all lowercase letters converted to uppercase. The function should not use any built-in string manipulation functions or methods. The input string can contain any characters, including punctuation, digits, and special characters.
"""

def convert_to_uppercase(string):
    uppercase_string = ""
    for char in string:
        if ord(char) >= 97 and ord(char) <= 122:
            uppercase_string += chr(ord(char) - 32)
        else:
            uppercase_string += char
    return uppercase_string