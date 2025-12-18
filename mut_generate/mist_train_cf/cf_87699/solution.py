"""
QUESTION:
Write a function `find_ascii_code(string)` that takes a string of up to 10^6 characters as input and returns the ASCII code of the character 'X' if found, and -1 otherwise. The function should have a time complexity of O(n), where n is the length of the string, and should not use any built-in functions or libraries for ASCII code conversion.
"""

def find_ascii_code(string):
    for char in string:
        if char == 'X':
            return ord(char)
    return -1