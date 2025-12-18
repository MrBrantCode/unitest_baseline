"""
QUESTION:
Create a function `is_palindrome(s)` that takes a string `s` as input and returns `True` if the string is a palindrome, ignoring non-alphanumeric characters and case sensitivity, and `False` otherwise. The function should also handle strings with leading or trailing spaces.
"""

def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    s = ''.join(e for e in s if e.isalnum()).lower()
    
    # Reverse the string and check if it is equal to the original string
    return s == s[::-1]