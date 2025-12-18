"""
QUESTION:
Write a function `is_palindrome(string)` that checks if a given string is a palindrome. The function should not use any built-in string manipulation functions and should perform a case-insensitive comparison, ignoring any non-alphanumeric characters and whitespace.
"""

def is_palindrome(string):
    string = string.lower()
    string = ''.join(filter(str.isalnum, string))
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True