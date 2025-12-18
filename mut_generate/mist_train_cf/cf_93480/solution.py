"""
QUESTION:
Write a function `is_palindrome(s)` that checks whether a given string `s` is a palindrome. The function should ignore case sensitivity and non-alphanumeric characters. It should return `True` if the string is a palindrome and `False` otherwise.
"""

def is_palindrome(s):
    # Step 1: Convert the input string to lowercase
    s = s.lower()
    
    # Step 2: Remove non-alphanumeric characters
    s = ''.join(ch for ch in s if ch.isalnum())
    
    # Step 3: Initialize pointers
    left = 0
    right = len(s) - 1
    
    # Step 4-7: Compare characters at pointers
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    # Step 8: Return True if pointers meet or cross
    return True