"""
QUESTION:
Write a function `is_palindrome(string)` that determines if the input string is a palindrome, ignoring spaces, punctuation, and capitalization, but considering non-alphabetic characters as part of the palindrome. The function should return `True` if the string is a palindrome and `False` otherwise. The solution should have a time complexity of O(n) and a space complexity of O(1).
"""

def is_palindrome(s):
    s = ''.join(c for c in s if c.isalnum()).lower()
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True