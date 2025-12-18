"""
QUESTION:
Write a function `count_alphabets(input_string)` that takes a string as input and returns the number of alphabets in the string, ignoring any punctuation marks and special characters. The function should handle uppercase and lowercase letters as separate entities and only consider the English alphabet.
"""

import string

def count_alphabets(input_string):
    # Remove any whitespace characters
    input_string = input_string.replace(" ", "")

    # Remove punctuation marks and special characters
    input_string = ''.join(char for char in input_string if char.isalpha())

    # Check each character in the string
    count = sum(1 for char in input_string if char.isalpha())
    
    return count