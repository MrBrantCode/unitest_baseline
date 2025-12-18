"""
QUESTION:
Write a function `is_palindrome` that takes a string `s` as input, returns `True` if `s` is a palindrome and `False` otherwise. The function should ignore special characters and consider case sensitivity.
"""

def is_palindrome(s):
    # Removing special characters and converting to lowercase
    clean_string = ''.join(ch.lower() for ch in s if ch.isalnum())

    # Comparing the clean string with its reverse
    return clean_string == clean_string[::-1]