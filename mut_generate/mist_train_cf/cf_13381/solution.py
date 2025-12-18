"""
QUESTION:
Create a function `is_palindrome` that determines if a given string is a palindrome. The function should have a time complexity of O(n), where n is the length of the string, and should not use built-in string reversal functions or additional data structures (except for temporary variables). The function should be case-insensitive.
"""

def is_palindrome(s):
    s = s.lower()
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True