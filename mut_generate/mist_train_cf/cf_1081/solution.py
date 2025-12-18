"""
QUESTION:
Create a function called `is_palindrome` that takes a string `s` as input. The function should return `True` if the string is a palindrome and `False` otherwise, ignoring non-alphanumeric characters and being case-insensitive. It should also handle strings with leading or trailing spaces. Do not use built-in string manipulation functions such as `reverse()` or slicing operator `[::-1]`.
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