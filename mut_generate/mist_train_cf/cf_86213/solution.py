"""
QUESTION:
Implement a function `is_valid_palindrome(s)` that takes a string `s` as input and returns `True` if the string is a valid palindrome, ignoring non-alphabetic characters and considering only lowercase alphabets, and `False` otherwise. The function should have a time complexity of O(n), where n is the length of the string.
"""

def is_valid_palindrome(s):
    s = s.lower()
    left = 0
    right = len(s) - 1
    
    while left < right:
        if not s[left].isalpha():
            left += 1
            continue
        
        if not s[right].isalpha():
            right -= 1
            continue
        
        if s[left] != s[right]:
            return False
        
        left += 1
        right -= 1
    
    return True