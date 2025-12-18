"""
QUESTION:
Write a function named `reverse_uppercase_string` that takes a string as input, removes all spaces, converts the string to uppercase, reverses the order of the characters, and returns the resulting string.
"""

def reverse_uppercase_string(input_string):
    return input_string.replace(" ", "").upper()[::-1]