"""
QUESTION:
Create a function `is_palindrome(word)` that checks if a given string `word` is a palindrome or not. Return "Palindrome" if the word is the same forwards and backwards, and "Not a palindrome" otherwise.
"""

def entrance(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return "Palindrome"
    else:
        return "Not a palindrome"