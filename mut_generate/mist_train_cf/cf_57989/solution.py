"""
QUESTION:
Write a function `sentences_palindrome(s1, s2)` that takes two sentences `s1` and `s2` as input and returns `True` if they are palindromes of each other, ignoring punctuation, spaces, and case sensitivity, and `False` otherwise.
"""

def sentences_palindrome(s1, s2):
    # Removing punctuation, spaces, case sensitivity
    s1 = ''.join(c for c in s1 if c.isalnum()).lower()
    s2 = ''.join(c for c in s2 if c.isalnum()).lower()

    # Checking if they are palindrome of each other
    return s1 == s2[::-1]