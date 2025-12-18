"""
QUESTION:
Write a function `is_palindrome(s)` that takes a string `s` as input and returns a boolean value indicating whether the string is a palindrome or not. The function should ignore non-alphabet characters and consider the string as a palindrome if it is a palindrome when read forwards and backwards, including considering each letter's Unicode code point, and in a case-insensitive manner.
"""

def is_palindrome(s):
    # Remove non-alphabet characters
    s = ''.join(c for c in s if c.isalpha())

    # Convert to lowercase
    s = s.lower()

    # Check if string is a palindrome
    return s == s[::-1]