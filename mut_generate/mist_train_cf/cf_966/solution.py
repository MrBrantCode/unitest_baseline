"""
QUESTION:
Implement a function `is_palindrome(s)` that checks if the input string `s` is a palindrome. The function should return `True` if the input string is a palindrome and `False` otherwise. The function should be case-insensitive, ignoring any non-alphanumeric characters in the input string. The implementation should have a time complexity of O(n) and a space complexity of O(1), without using any built-in functions or libraries that directly solve the problem.
"""

def entrance(s):
    # Remove non-alphanumeric characters and convert to lowercase
    s = ''.join(c.lower() for c in s if c.isalnum())
    
    # Check if the string is a palindrome
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True