"""
QUESTION:
Implement a function `convert_to_uppercase` that takes a string as input and returns a new string where all lowercase letters are converted to uppercase. The function should not use any built-in functions or methods that directly convert a string to upper case, and should leave non-alphabetic characters and uppercase letters unchanged. The time complexity should be O(n), where n is the length of the input string.
"""

def convert_to_uppercase(string):
    uppercase_string = ""
    for char in string:
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_string += chr(ord(char) - ord('a') + ord('A'))
        else:
            uppercase_string += char
    return uppercase_string