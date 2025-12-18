"""
QUESTION:
Create a function `is_palindrome(s)` that determines if a given string `s` is a palindrome, ignoring case and spaces. The function should return `True` if the string is a palindrome and `False` otherwise. The input string `s` will contain only letters and spaces.
"""

def entrance(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]