"""
QUESTION:
Write a function named `is_palindrome` that takes a string as input and returns `True` if the string is a palindrome, considering only alphanumeric characters and ignoring case, spaces, and special characters, and `False` otherwise.
"""

def is_palindrome(s):
    # Remove special characters and convert to lowercase
    s = ''.join(e for e in s if e.isalnum()).lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]