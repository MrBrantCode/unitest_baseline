"""
QUESTION:
Write a function `is_palindrome(string)` that checks if a given string is a palindrome. The function should remove leading/trailing whitespace, perform case-insensitive comparison, and not use any built-in string manipulation functions. It should return `True` if the string is a palindrome and `False` otherwise.
"""

def is_palindrome(string):
    string = string.strip().lower()
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True