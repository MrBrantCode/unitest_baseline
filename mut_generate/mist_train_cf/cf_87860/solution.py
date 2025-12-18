"""
QUESTION:
Write a Python function `transform_to_uppercase` that takes a string as input, transforms all alphabetic characters to upper case, and returns the modified string. The function should handle strings with any combination of upper case and lower case letters, non-alphabetic characters, special characters, and symbols, without using built-in string manipulation functions or libraries. The function should have a time complexity of O(n) and a space complexity of O(1).
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