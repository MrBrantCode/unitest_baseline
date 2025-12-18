"""
QUESTION:
Write a function `is_palindrome(s)` that takes a string `s` as input and returns a boolean value indicating whether the string is a palindrome, ignoring non-alphabetic characters and case.
"""

def is_palindrome(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    return s == s[::-1]