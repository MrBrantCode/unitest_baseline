"""
QUESTION:
Write a function `is_palindrome(s)` that determines whether a given string `s` is a palindrome, ignoring special characters and considering alphanumeric characters case-insensitively. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the string.
"""

def is_palindrome(s):
    left = 0
    right = len(s) - 1

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