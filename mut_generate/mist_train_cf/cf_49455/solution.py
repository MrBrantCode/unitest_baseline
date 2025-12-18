"""
QUESTION:
Create a function named `is_palindrome` that takes a string `s` as input and returns `True` if `s` is a palindrome and `False` otherwise. The function should consider a string with spaces as a palindrome if its non-space characters read the same backward as forward, and should be case-sensitive.
"""

def is_palindrome(s):
    s = s.replace(' ', '')  
    return s == s[::-1]