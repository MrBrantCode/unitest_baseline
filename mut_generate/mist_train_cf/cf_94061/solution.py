"""
QUESTION:
Create a function called `is_palindrome` that takes a string as input and returns True if the string is a palindrome, ignoring non-alphanumeric characters and being case-insensitive, and False otherwise. The function should also handle strings with leading or trailing spaces without using any built-in string manipulation functions such as `reverse()`.
"""

def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True