"""
QUESTION:
Write a function `is_palindrome` that takes a string as input and returns a boolean indicating whether the string is a palindrome or not. The function must have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1), without using any built-in string manipulation functions or data structures.
"""

def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left <= right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True