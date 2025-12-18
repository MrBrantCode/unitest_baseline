"""
QUESTION:
Write a function `is_palindrome(s)` that takes a string `s` as input and returns `True` if it is a palindrome, ignoring spaces, punctuation marks, and case sensitivity. The function should not use any built-in string reversal functions or libraries, and its time complexity should be less than O(n^2).
"""

import string

def is_palindrome(s):
    # Remove spaces, punctuation marks, and convert to lowercase
    s = s.translate(str.maketrans('', '', string.punctuation)).replace(" ", "").lower()
    
    # Check if the string is a palindrome
    start = 0
    end = len(s) - 1
    
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    
    return True