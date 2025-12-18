"""
QUESTION:
Implement a function named `isPalindrome` that checks whether a given string is a palindrome or not. The function should ignore non-alphanumeric characters, be case-insensitive, and have a time complexity of O(n), where n is the length of the string. The solution must be done in-place with constant extra space, without using any additional data structures.
"""

def isPalindrome(s):
    s = s.lower()
    left = 0
    right = len(s) - 1
    
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        else:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
    
    return True