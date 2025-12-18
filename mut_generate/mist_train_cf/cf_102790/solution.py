"""
QUESTION:
Write a function `repeat_last_two` that takes a string of 2-100 characters as input and returns the input string with its last two characters repeated. The function should handle strings containing special characters and whitespace.
"""

def repeat_last_two(string):
    last_two_chars = string[-2:]
    return string + last_two_chars