"""
QUESTION:
Implement a function named `is_palindrome(s)` that takes a string `s` as input and returns a boolean indicating whether the string is a palindrome or not. The function should be case-insensitive, ignore punctuation and whitespace, and handle alphanumeric characters. The solution should have a time complexity of O(n) and use constant extra space, where n is the length of the input string.
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