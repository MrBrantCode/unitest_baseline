"""
QUESTION:
Write a function `is_palindrome(s)` that checks if a given string `s` is a palindrome. The function should have a time complexity of O(n) and a space complexity of O(1). The function should return `True` if the string is a palindrome, and `False` otherwise.
"""

def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True