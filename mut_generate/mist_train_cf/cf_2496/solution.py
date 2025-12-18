"""
QUESTION:
Write a function `is_palindrome(s)` to detect if a given string `s` is a palindrome or not. The function should consider only alphanumeric characters and ignore case. It should achieve a linear time complexity.
"""

def is_palindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True