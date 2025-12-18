"""
QUESTION:
Write a function `contains_palindrome(words)` that takes a list of strings as input and returns `True` if the list contains at least one palindrome word, and `False` otherwise.
"""

def contains_palindrome(words):
    for word in words:
        if word == word[::-1]:
            return True
    return False