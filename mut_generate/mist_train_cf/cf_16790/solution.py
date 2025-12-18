"""
QUESTION:
Write a function `is_palindrome(s)` that takes a string `s` as input and returns `True` if the string is a palindrome and `False` otherwise. The function should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1).
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