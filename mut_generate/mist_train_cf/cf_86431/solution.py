"""
QUESTION:
Write a function named `convert_to_uppercase` that takes a string as input and returns the string in uppercase without using any built-in string manipulation functions or methods. The function should handle special characters, numbers, and whitespace, and have a time complexity of O(n), where n is the length of the input string.
"""

def convert_to_uppercase(string):
    result = ""
    for char in string:
        # Check if character is a lowercase letter
        if ord('a') <= ord(char) <= ord('z'):
            # Convert lowercase letter to uppercase by subtracting 32 from its ASCII value
            char = chr(ord(char) - 32)
        result += char
    return result