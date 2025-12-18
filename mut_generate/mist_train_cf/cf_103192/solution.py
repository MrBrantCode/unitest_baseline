"""
QUESTION:
Design a function `convert_to_string` that takes an array of characters as input and returns a string containing only the alphabetic characters (A-Z) from the array, ignoring any other characters.
"""

def convert_to_string(char_array):
    result = ''
    for char in char_array:
        if char.isalpha():
            result += char
    return result