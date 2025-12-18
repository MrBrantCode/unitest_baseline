"""
QUESTION:
Write a function `find_ascii_code` that takes a string as input and returns the ASCII code of the character 'X' if it exists in the string. The function should have a time complexity of O(n), where n is the length of the string, and should not use any built-in functions or libraries for ASCII code conversion, except for the ord() function which is allowed.
"""

def find_ascii_code(string):
    for char in string:
        if char == 'X':
            return ord(char)
    return -1  # If 'X' is not found in the string