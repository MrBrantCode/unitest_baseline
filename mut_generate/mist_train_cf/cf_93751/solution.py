"""
QUESTION:
Write a function `convert_to_uppercase` that takes a string as input and returns the string with all lowercase letters converted to uppercase without using any built-in string manipulation functions or methods. The function should only use a single loop and have a time complexity of O(n), where n is the length of the input string. The function should handle non-alphabetic characters by leaving them unchanged in the output string.
"""

def convert_to_uppercase(string):
    converted_string = ""
    for char in string:
        if ord('a') <= ord(char) <= ord('z'):
            char = chr(ord(char) - ord('a') + ord('A'))
        converted_string += char
    return converted_string