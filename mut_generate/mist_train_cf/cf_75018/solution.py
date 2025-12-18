"""
QUESTION:
Write a function called `is_palindrome` that takes one string as input and returns a boolean value indicating whether the input string is the same forwards and backwards.
"""

def is_palindrome(input_str):
    return input_str == input_str[::-1]