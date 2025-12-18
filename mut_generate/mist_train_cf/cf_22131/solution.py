"""
QUESTION:
Write a function `is_palindrome(s)` that takes a string `s` as input and checks if it is a palindrome. The function should ignore any non-alphanumeric characters and consider the string as case-insensitive. It should also handle multi-line input. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string. Return `True` if the input is a palindrome, and `False` otherwise.
"""

import re

def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    
    # Check if the string is a palindrome
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True