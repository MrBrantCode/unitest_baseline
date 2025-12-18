"""
QUESTION:
Write a function `reverse_binary_string` that takes a string as input, removes all punctuation marks and special characters, converts each remaining character to its binary representation, reverses the order of the characters in the string, and returns the resulting binary string.

The function should run in O(n) time complexity and O(1) space complexity, where n is the length of the input string.
"""

import re

def reverse_binary_string(string):
    # Remove punctuation marks and special characters
    string = re.sub(r'[^\w\s]', '', string)
    
    binary_string = ''
    for char in reversed(string):
        binary_char = bin(ord(char))[2:]  # Convert character to binary
        binary_string += binary_char
    
    return binary_string