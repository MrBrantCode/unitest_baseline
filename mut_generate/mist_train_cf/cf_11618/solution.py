"""
QUESTION:
Create a function called `is_string_palindrome` that takes one string argument and returns `True` if the string is the same when its characters are reversed, and `False` otherwise.
"""

def is_string_palindrome(string):
    return string == string[::-1]