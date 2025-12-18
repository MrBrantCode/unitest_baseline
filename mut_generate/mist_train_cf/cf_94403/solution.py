"""
QUESTION:
Write a function named `is_palindrome(s)` that determines whether a given string `s` is a palindrome or not. The function should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1), meaning it should only use a constant amount of additional memory.
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