"""
QUESTION:
Design a function `is_palindrome` that checks if a given string is a palindrome, considering only alphanumeric characters and ignoring case, spaces, and punctuation.
"""

def is_palindrome(s: str) -> bool:
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]