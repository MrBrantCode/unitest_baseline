"""
QUESTION:
Write a function called `reverse_string` that takes a string `input_str` as input and returns its reverse without using any built-in functions or methods that directly reverse a string. The function should handle special characters and whitespace, and preserve the original case of each character in the reversed string.
"""

def entance(input_str):
    reversed_str = ''
    for char in input_str:
        reversed_str = char + reversed_str
    return reversed_str