"""
QUESTION:
Write a function called `transform_to_uppercase` that takes a string as input, converts all alphabetic characters in the string to uppercase, and returns the modified string without using built-in string manipulation functions or libraries. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string.
"""

def transform_to_uppercase(string):
    modified_string = ""
    for char in string:
        if char.isalpha():
            if char >= 'a' and char <= 'z':
                char = chr(ord(char) - 32)
            elif char >= 'à' and char <= 'ÿ':
                char = chr(ord(char) - 32)
        modified_string += char
    return modified_string