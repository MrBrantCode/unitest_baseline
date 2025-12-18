"""
QUESTION:
Write a function named `convert_to_uppercase` that takes a string as input and returns a new string where all lowercase letters in the input string are converted to uppercase, while keeping all other characters unchanged. The function should not use built-in string conversion functions, should have a time complexity of O(n), and should not modify the original string.
"""

def convert_to_uppercase(string):
    uppercase_string = ""
    for char in string:
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_string += chr(ord(char) - ord('a') + ord('A'))
        else:
            uppercase_string += char
    return uppercase_string