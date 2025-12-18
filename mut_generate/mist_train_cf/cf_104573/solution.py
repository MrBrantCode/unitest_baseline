"""
QUESTION:
Write a function `is_palindrome(string)` that checks if a given string can be converted to a palindrome, considering only alphanumeric characters and ignoring the case. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string.
"""

def entrance(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    
    return True