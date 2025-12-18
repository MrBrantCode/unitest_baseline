"""
QUESTION:
Create a function `is_palindrome` that takes a string as input and returns a boolean value indicating whether the string is a palindrome. The function should be case-insensitive, ignore non-alphanumeric characters, and have a time complexity of O(n) and a space complexity of O(1). The implementation should not use built-in string manipulation or comparison functions.
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