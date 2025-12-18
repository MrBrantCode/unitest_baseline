"""
QUESTION:
Write a function `is_palindrome(s)` that takes a string `s` as input and returns `True` if the string is a palindrome, and `False` otherwise. The function must be case-sensitive and have a time complexity of O(n), where n is the length of the input string.
"""

def is_palindrome(s):
    start = 0
    end = len(s) - 1
    
    while start < end:
        if s[start] != s[end]:
            return False
        
        start += 1
        end -= 1
    
    return True