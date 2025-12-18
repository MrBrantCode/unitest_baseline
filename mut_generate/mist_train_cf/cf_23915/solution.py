"""
QUESTION:
Write a function `is_palindrome` that checks if a given sentence is a palindrome. The function should ignore spaces and return True if the sentence is a palindrome, False otherwise.
"""

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]