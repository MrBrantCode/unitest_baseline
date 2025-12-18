"""
QUESTION:
Write a function `is_palindrome(s)` that checks whether a given input string `s` is a palindrome or not. The function should be case-insensitive and ignore punctuation and whitespace. It should also handle palindromes with numbers. The function must solve the problem in-place with constant extra space and have a time complexity of O(n), where n is the length of the input string.
"""

def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True