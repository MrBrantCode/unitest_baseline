"""
QUESTION:
Write a function `is_palindrome(word)` that takes a string `word` as input and returns a boolean indicating whether the string is a palindrome, i.e., it reads the same forward and backward, ignoring spaces, punctuation, and capitalization.
"""

def is_palindrome(word):
    word = ''.join(e for e in word if e.isalnum()).lower()
    return word == word[::-1]