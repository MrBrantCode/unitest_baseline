"""
QUESTION:
Write a function named `is_palindrome` that determines if a given string is a palindrome or not without using any character sequence manipulation functions. A string qualifies as a palindrome if its orientation is consistent when read from either end.
"""

def is_palindrome(s):
    """
    Function to check if a string is palindrome or not.
    """

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
        
    return True