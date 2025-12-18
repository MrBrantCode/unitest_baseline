"""
QUESTION:
Implement a function named `is_palindrome` that takes a string `s` as input and returns `True` if it is a palindrome and `False` otherwise. The function should consider only alphanumeric characters, ignore case sensitivity, and exclude spaces, special characters, and punctuation marks. The implementation must have a time complexity of O(n) and use recursion instead of iteration.
"""

def is_palindrome(s):
    if len(s) <= 1:
        return True

    if not s[0].isalnum():
        return is_palindrome(s[1:])
    elif not s[-1].isalnum():
        return is_palindrome(s[:-1])

    if s[0].lower() != s[-1].lower():
        return False

    return is_palindrome(s[1:-1])