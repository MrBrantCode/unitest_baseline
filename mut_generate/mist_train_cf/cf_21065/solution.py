"""
QUESTION:
Create a function called `is_palindrome` that takes a string as input and returns `True` if the string is a palindrome, otherwise returns `False`. The function should have a time complexity of O(n), where n is the length of the string, and should not use any built-in string reversal functions or methods, or additional data structures except for temporary variables if necessary. The function should be case-insensitive, consider alphanumeric characters only, and ignore any other characters such as spaces, punctuation marks, and special characters. It should also handle non-Latin characters, such as accented characters.
"""

def is_palindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True