"""
QUESTION:
Create a function named `is_palindrome` that takes a string `s` as input and returns `True` if the string is a palindrome (ignoring case, spaces, and punctuation) and `False` otherwise. The function should be case-insensitive and should ignore any non-alphanumeric characters.
"""

def is_palindrome(s):
    stripped_string = ''.join(e for e in s if e.isalnum()).lower()
    return stripped_string == stripped_string[::-1]