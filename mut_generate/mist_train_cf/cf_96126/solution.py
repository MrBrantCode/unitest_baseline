"""
QUESTION:
Write a function `remove_char(string, char)` that takes two parameters: a string and a character. The function should return a new string where all occurrences of the specified character are removed from the input string. Do not use any built-in string manipulation functions or libraries.
"""

def entrance(string, char):
    result = ""
    for c in string:
        if c != char:
            result += c
    return result