"""
QUESTION:
Write a Python function named `transform_to_upper` that takes a string as input and transforms all alphabetic characters of the string to upper case without using built-in string manipulation functions or libraries. The function should not modify any non-alphabetic characters and should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string.
"""

def transform_to_upper(string):
    modified_string = ""
    for char in string:
        if 'a' <= char <= 'z':
            modified_string += chr(ord(char) - 32)
        else:
            modified_string += char
    return modified_string