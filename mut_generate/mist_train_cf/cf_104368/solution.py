"""
QUESTION:
Write a Python function `reverse_string` that takes a string of at least 3 characters as input. The function should return the second character of the string, the reversed string in uppercase, and a tuple containing the reversed string and its length.
"""

def reverse_string(s):
    second_char = s[1]
    reversed_string = s[::-1].upper()
    length = len(reversed_string)
    return second_char, reversed_string, (reversed_string, length)