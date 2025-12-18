"""
QUESTION:
Write a function called `verify_string_length` that checks if the length of the input string is between 5 and 20 characters (inclusive). The function should return `True` if the string length is within this range and `False` otherwise.
"""

def verify_string_length(input_string):
    return 5 <= len(input_string) <= 20