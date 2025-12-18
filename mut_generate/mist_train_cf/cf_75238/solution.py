"""
QUESTION:
Determine if a given string is a palindrome using a function named `is_palindrome` without utilizing any built-in library functions, special characters, or additional data structures.
"""

def is_palindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True