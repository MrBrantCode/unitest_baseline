"""
QUESTION:
Implement a function `is_palindrome(s, start=0)` that takes a string `s` and returns a boolean indicating whether the string is a palindrome or not. The function should ignore special characters, punctuation, and case, and must be implemented recursively without using slicing to reverse the string.
"""

def entrance(s, start=0):
    s_without_specials = ''.join(e for e in s if e.isalnum()).lower()
    end = len(s_without_specials) - 1 - start
    if start >= end:
        return True
    elif s_without_specials[start] != s_without_specials[end]:
        return False
    return entrance(s, start+1)