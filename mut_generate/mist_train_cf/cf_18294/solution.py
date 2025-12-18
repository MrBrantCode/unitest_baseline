"""
QUESTION:
Create a function named `is_palindrome(word)` that checks whether a given string is a palindrome or not. The function should return "Palindrome" if the string is the same when its characters are reversed, and "Not a palindrome" otherwise. The function should be case sensitive and consider spaces and punctuation as part of the string.
"""

def is_palindrome(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return "Palindrome"
    else:
        return "Not a palindrome"