"""
QUESTION:
Write a function named `reverse_binary_string` that takes a string as input, ignores any punctuation marks or special characters, and returns its binary representation with the binary representation reversed. The function should have a time complexity of O(n) and space complexity of O(1), where n is the length of the input string.
"""

import re

def reverse_binary_string(string):
    string = re.sub(r'[^\w\s]', '', string)
    binary_string = ''
    for char in reversed(string):
        binary_char = bin(ord(char))[2:]  
        binary_string += binary_char
    return binary_string