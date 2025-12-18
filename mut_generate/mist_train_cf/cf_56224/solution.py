"""
QUESTION:
Write a function `string_palindrome(s: str)` that determines whether a given non-empty string `s` is a palindrome, disregarding spaces, punctuation, and capitalization, and only analyzing half the characters of `s` for efficiency. The function should return `True` if the string is a palindrome and `False` otherwise.
"""

def is_palindrome(s: str) -> bool:
    s = [c.lower() for c in s if c.isalnum()]
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True