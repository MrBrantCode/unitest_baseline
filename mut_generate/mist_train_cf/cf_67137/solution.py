"""
QUESTION:
Write a recursive function `is_palindrome(s, ignore_chars=None)` that checks whether a given string `s` is a palindrome or not, optionally ignoring specified characters in `ignore_chars`. The function should return a boolean value indicating whether `s` is a palindrome, and it should be case insensitive.
"""

def entrance(s, ignore_chars=None):
    s = s.lower()
    if ignore_chars:
        s = ''.join(ch for ch in s if ch not in ignore_chars)
        
    # Recursive case: s is a palindrome if first and last chars are the same, and middle is a palindrome.
    if len(s) <= 1: 
        return True
    elif s[0] != s[-1]: 
        return False
    else: 
        return entrance(s[1:-1])