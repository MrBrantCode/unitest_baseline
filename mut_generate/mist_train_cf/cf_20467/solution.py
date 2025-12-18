"""
QUESTION:
Write a function `remove_char` that takes a string and a character as input and returns a new string with all occurrences of the character removed from the original string. Do not use any built-in string manipulation functions or libraries.
"""

def remove_char(string, char):
    result = ""
    for c in string:
        if c != char:
            result += c
    return result