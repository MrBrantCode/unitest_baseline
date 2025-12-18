"""
QUESTION:
Create a function `remove_empty_spaces_and_punctuation` that takes a string as input and returns a new string with all empty spaces and punctuation removed. The function should handle multiple occurrences of empty spaces and punctuation, have a time complexity of O(n) where n is the length of the input string, and not use any built-in string manipulation functions or regular expressions.
"""

def remove_empty_spaces_and_punctuation(string):
    result = ""
    for char in string:
        if char.isalnum():
            result += char
    return result