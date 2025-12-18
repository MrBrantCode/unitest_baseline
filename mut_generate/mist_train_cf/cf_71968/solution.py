"""
QUESTION:
Create a function `is_palindrome(s)` that checks if a given string `s` is a palindrome, i.e., it reads the same backward as forward. The function should return `True` if the string is a palindrome and `False` otherwise. The function should only consider the input string `s` and should not use any additional inputs or parameters.
"""

def is_palindrome(s):
    return s == s[::-1]