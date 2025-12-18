"""
QUESTION:
Create a function called `remove_whitespace_and_punctuation` that takes a string as input and returns the string without whitespace and punctuation marks. The function should be case-insensitive and able to handle non-English characters. It should not use built-in string manipulation functions or regular expressions.
"""

def remove_whitespace_and_punctuation(string):
    punctuation_marks = ['.', ',', '?', '!', ';', ':', '-', '_', '(', ')', '[', ']', '{', '}', '<', '>', '/', '\\', '|', '@', '#', '$', '%', '^', '&', '*', '~', '`', '+', '=', '"']
    whitespace = [' ', '\t', '\n', '\r']
    clean_string = ""
    for char in string:
        if char.lower() not in punctuation_marks and char.lower() not in whitespace:
            clean_string += char
    return clean_string