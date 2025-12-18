"""
QUESTION:
Write a function `is_palindrome(s)` that determines whether a given string `s` is a palindrome or not. The function should be case-insensitive, ignore whitespace characters and punctuation marks, and handle strings with both uppercase and lowercase letters, whitespace characters, punctuation marks, numbers, special characters, non-English characters, and HTML tags. The function should not use any built-in functions or libraries that directly check for palindromes or reverse strings, and it should have a time complexity of O(n), where n is the length of the input string.
"""

def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    s = ''.join(char for char in s if char != '<' and char != '>')
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left, right = left + 1, right - 1
    return True