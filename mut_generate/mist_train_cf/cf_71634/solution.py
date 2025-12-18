"""
QUESTION:
Create a function named `is_palindrome(s)` that determines whether a given string `s` is a palindrome. The function should ignore non-alphanumeric characters and be case-insensitive.
"""

def is_palindrome(s):
    """
    Function to check if a string is palindrome or not.
    An empty string is considered as palindrome.
    """
    s_alphanum = [char.lower() for char in s if char.isalnum()]
    return s_alphanum == s_alphanum[::-1]