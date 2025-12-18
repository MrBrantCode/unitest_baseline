"""
QUESTION:
Create a function `is_palindrome` that determines if a given string is a palindrome. The function should not use any built-in string manipulation functions or methods and should not use any extra data structures such as arrays or lists. The function should return `True` if the string is a palindrome and `False` otherwise.
"""

def is_palindrome(s):
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            return False
    return True