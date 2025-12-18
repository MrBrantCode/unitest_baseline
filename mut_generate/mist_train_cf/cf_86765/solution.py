"""
QUESTION:
Write a function `is_palindrome(s)` that takes a string `s` as input and returns `True` if it is a palindrome and `False` otherwise. The function should be case-insensitive, ignore non-alphanumeric characters, and handle leading or trailing spaces without using built-in string manipulation functions such as `reverse()` or slicing with a step of -1.
"""

def is_palindrome(s):
    # Removing non-alphanumeric characters and converting to lowercase
    s = ''.join(ch.lower() for ch in s if ch.isalnum())

    # Handling leading or trailing spaces
    s = s.strip()

    # Checking if the string is a palindrome
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True