"""
QUESTION:
Write a function `is_palindrome(s)` that takes a string `s` as input and returns `True` if the string is the same when its characters are reversed, and `False` otherwise. The function should not use any built-in Python functions or methods.
"""

def is_palindrome(s):
    # Reverse the string
    reversed_str = s[::-1]
    # Checking if both string are equal or not
    if (s == reversed_str):
        return True
    return False