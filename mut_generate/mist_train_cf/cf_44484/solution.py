"""
QUESTION:
Design a function called `is_palindrome` that determines if a given string is a palindrome, ignoring non-alphanumeric characters, spaces, and case sensitivity. The function should take a string `s` as input and return `True` if it is a palindrome and `False` otherwise.
"""

def is_palindrome(s):
    s = ''.join(c for c in s if c.isalnum()).lower() 
    return s == s[::-1]