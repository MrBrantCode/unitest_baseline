"""
QUESTION:
Create a function `transform_string` that takes a string as input, removes all spaces, converts all letters to uppercase, and reverses the order of characters. The function should achieve this in a single line of code, have a time complexity of O(n), and not use any built-in string manipulation functions or methods.
"""

def transform_string(s):
    return ''.join([char.upper() for char in s if char != ''])[::-1]