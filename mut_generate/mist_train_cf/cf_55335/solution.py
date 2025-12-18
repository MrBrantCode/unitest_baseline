"""
QUESTION:
Write a `PalindromeChecker` class with an `is_palindrome` method that takes a string as input, removes non-alphanumeric characters, and converts the string to lowercase. The method should return True if the resulting string is the same when reversed, and False otherwise. The input string may contain spaces and punctuation.
"""

def is_palindrome(s):
    # Removing all non-alphanumeric characters from the string
    s = ''.join(e for e in s if e.isalnum())
    s = s.lower()
    
    # Reverse and compare
    return s == s[::-1]