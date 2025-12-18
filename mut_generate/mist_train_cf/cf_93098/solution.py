"""
QUESTION:
Write a function `is_palindrome(s)` that checks if a given string `s` is a palindrome. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the string. The function should return `True` if the string is a palindrome and `False` otherwise.
"""

def entance(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True