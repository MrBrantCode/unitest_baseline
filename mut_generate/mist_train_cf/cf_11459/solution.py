"""
QUESTION:
Implement a function `is_palindrome(s: str) -> bool` that checks whether the input string `s` is a palindrome. The function should be case-insensitive, ignore non-alphanumeric characters, and have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string. The function should use a regular expression to check if the input string is a palindrome.
"""

import re

def is_palindrome(s: str) -> bool:
    # Remove non-alphanumeric characters and convert to lowercase
    s = re.sub(r'\W+', '', s).lower()
    
    # Use two pointers to check if the string is a palindrome
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True