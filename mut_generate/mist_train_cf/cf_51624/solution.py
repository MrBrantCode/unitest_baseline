"""
QUESTION:
Write a function `is_palindrome(s)` that takes a string `s` as input. The function should return `True` if the string is a palindrome and `False` otherwise. The palindrome check should be case insensitive and ignore spaces and punctuation.
"""

def is_palindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()    # Ignore punctuation and spaces, convert to lowercase
    rev = s[::-1]    # Reverse the string
    return s == rev   # Check for palindrome