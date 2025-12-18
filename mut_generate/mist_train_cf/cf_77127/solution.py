"""
QUESTION:
Create a function called `is_palindrome(word)` that determines whether a given word is a palindrome or not. The function should take a string `word` as input and return a boolean value indicating whether the word is the same when its letters are reversed.
"""

def is_palindrome(word):
    return word == word[::-1]