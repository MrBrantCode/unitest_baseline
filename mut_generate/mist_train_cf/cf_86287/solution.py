"""
QUESTION:
Write a function `is_palindrome(s)` that takes a string `s` and returns a boolean indicating whether the string is a palindrome or not. The function should ignore alphabetic case differences (case-insensitive) but consider non-alphabetic characters and numbers as part of the palindrome check. The function must have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string.
"""

def entrance(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True