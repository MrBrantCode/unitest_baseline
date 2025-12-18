"""
QUESTION:
Write a function `is_palindrome(s)` that determines whether a given string `s` is a palindrome or not. The function should ignore non-alphanumeric characters, consider alphanumeric characters case-insensitively, and handle strings with multiple words and spaces.
"""

def entrance(s):
    # Remove special characters and convert to lowercase
    s = ''.join(e for e in s if e.isalnum()).lower()

    # Check if the string is equal to its reverse
    return s == s[::-1]