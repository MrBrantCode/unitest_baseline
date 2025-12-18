"""
QUESTION:
Write a function named `get_length` that calculates the length of a given string without using built-in string length functions. The function should handle strings of any length and complexity, including special characters, numbers, whitespace, and escape sequences. It should also be able to decode strings encoded in non-standard character encoding formats and count the length of the decoded string.
"""

def get_length(input_string):
    length = 0
    for _ in input_string:
        length += 1
    return length