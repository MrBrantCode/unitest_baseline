"""
QUESTION:
Write a function `is_palindrome` that checks if a given string is a palindrome, ignoring special characters and considering only alphanumeric characters for the palindrome check. The function should perform a case-insensitive comparison and return `True` if the string is a palindrome, and `False` otherwise.
"""

def is_palindrome(s):
    # Removing special characters from the string
    s = ''.join(e for e in s if e.isalnum())
    
    # Converting string to lowercase for case-insensitive comparison
    s = s.lower()
    
    # Checking if the modified string is a palindrome
    return s == s[::-1]