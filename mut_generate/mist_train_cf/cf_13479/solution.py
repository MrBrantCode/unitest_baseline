"""
QUESTION:
Write a function `is_palindrome(s)` that checks if a given string `s` is a palindrome or not, ignoring case sensitivity and non-alphanumeric characters, without using extra space. The string `s` has at most 1000 characters.
"""

def entrance(s):
    s = s.lower()
    left = 0
    right = len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True