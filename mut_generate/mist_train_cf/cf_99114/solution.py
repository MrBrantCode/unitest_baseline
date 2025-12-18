"""
QUESTION:
Write a function `is_palindrome(word)` that determines if a given string is a palindrome using recursion. The function should ignore non-alphanumeric characters and be case-insensitive. Do not use built-in functions or libraries.
"""

def entance(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return entance(s[1:-1])