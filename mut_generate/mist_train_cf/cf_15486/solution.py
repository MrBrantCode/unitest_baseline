"""
QUESTION:
Write a function `convert_to_uppercase` that converts a given string to uppercase without using any built-in string manipulation functions or methods. The function should have a time complexity of O(n), where n is the length of the input string, and only use a single loop. The function should work with strings containing both alphabetic and non-alphabetic characters.
"""

def convert_to_uppercase(string):
    converted_string = ""
    for char in string:
        if ord('a') <= ord(char) <= ord('z'):
            char = chr(ord(char) - ord('a') + ord('A'))
        converted_string += char
    return converted_string