"""
QUESTION:
Write a function `get_first_last_unique_chars` that takes a string as input and returns a string containing the first and last occurring unique characters in sorted order. The function should handle strings containing special characters, numbers, and uppercase letters by treating uppercase letters as their lowercase equivalents and ignoring non-alphabetic characters.
"""

def get_first_last_unique_chars(string):
    # Remove special characters, numbers, and uppercase letters
    string = ''.join(ch.lower() for ch in string if ch.isalpha())
    
    # Find the first and last occurring unique characters
    first_unique = ''
    last_unique = ''
    for ch in string:
        if string.count(ch) == 1:
            if not first_unique:
                first_unique = ch
            last_unique = ch
    
    # Sort and return the first and last unique characters
    return ''.join(sorted([first_unique, last_unique]))