"""
QUESTION:
Write a function `is_palindrome(s)` that takes a string `s` as input and returns `True` if the string is a palindrome, and `False` otherwise. The function should be case-insensitive, ignore whitespace characters, and ignore punctuation marks. Do not use any built-in functions or libraries that directly check for palindromes or reverse strings.
"""

def is_palindrome(s):
    # Remove whitespace characters
    s = ''.join(s.split())

    # Remove punctuation marks
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    s = ''.join(ch for ch in s if ch not in punctuation)

    # Convert string to lowercase
    s = s.lower()

    # Check if the string is a palindrome
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            return False
    return True