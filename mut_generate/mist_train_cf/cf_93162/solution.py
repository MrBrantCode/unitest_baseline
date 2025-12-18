"""
QUESTION:
Write a function `is_palindrome(s)` that determines if a given string `s` is a palindrome. The function should ignore non-alphabet characters and be case-insensitive. The string is considered a palindrome if it reads the same forwards and backwards when only alphabet characters are considered. Return a boolean value indicating whether the string is a palindrome or not.
"""

def entrance(s):
    # Remove non-alphabet characters
    s = ''.join(c for c in s if c.isalpha())

    # Convert to lowercase
    s = s.lower()

    # Check if string is a palindrome
    return s == s[::-1]