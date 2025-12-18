"""
QUESTION:
Write a function named `reverse_string` that takes an input string and returns a string with its characters reversed, without using any built-in string reversal functions or libraries. The function should handle strings containing special characters and whitespace, and preserve the original case of each character.
"""

def entrance(input_str):
    reversed_str = ""
    for char in input_str:
        reversed_str = char + reversed_str
    return reversed_str