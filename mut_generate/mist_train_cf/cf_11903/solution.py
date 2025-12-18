"""
QUESTION:
Write a function `convert_string` that takes an input string and returns a new string with all characters converted to uppercase and all punctuation marks removed. The function should only use basic operations (no built-in functions or methods for case conversion) and have a time complexity of O(n), where n is the length of the input string. The input string will only contain alphabetic characters, spaces, and punctuation marks.
"""

def convert_string(string):
    uppercase_string = ""
    for char in string:
        if char.isalpha() or char.isspace():
            uppercase_string += char.upper()
    return uppercase_string