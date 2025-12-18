"""
QUESTION:
Create a function named `remove_empty_spaces_and_punctuation` that takes a string as input and returns a new string with all empty spaces and punctuation removed. The function should have a time complexity of O(n), where n is the length of the input string, and should not use any built-in string manipulation functions or regular expressions. The input string may contain any printable ASCII characters, including alphanumeric characters, special characters, and punctuation.
"""

def remove_empty_spaces_and_punctuation(string):
    result = ""
    for char in string:
        if char.isalnum():
            result += char
    return result