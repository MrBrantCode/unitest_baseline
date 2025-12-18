"""
QUESTION:
Write a function called `is_palindrome` that takes a string `s` as input. The function should return `True` if the input string is a palindrome and `False` otherwise. The function should be case-insensitive and ignore any whitespace characters and punctuation marks. The input string can contain both uppercase and lowercase letters, whitespace characters, and punctuation marks. No built-in functions or libraries that directly check for palindromes or reverse strings are allowed.
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