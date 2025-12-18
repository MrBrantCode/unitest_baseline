"""
QUESTION:
Write a function named `is_palindrome` that takes a string `s` as input and returns a boolean value indicating whether the string is a palindrome or not. The function should ignore spaces and punctuation marks in the string and be case-insensitive. The time complexity of the function should be less than O(n^2).
"""

def is_palindrome(s):
    s = ''.join(c for c in s if c.isalnum()).lower()
    start = 0
    end = len(s) - 1
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True