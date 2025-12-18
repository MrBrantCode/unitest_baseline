"""
QUESTION:
Write a Python function named `reverse_string` that takes an input string and returns the string with its characters in reverse order. The function should use slicing and support strings of any length. The input string can contain any type of characters, including punctuation and spaces.
"""

def reverse_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string