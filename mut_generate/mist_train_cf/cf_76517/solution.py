"""
QUESTION:
Write a function `is_palindrome` that filters a list of textual elements and returns a list of words that are palindromes, where a palindrome is a text that remains the same when its characters are reversed. The function should take a list of strings as input and return a list of strings.
"""

def is_palindrome(word_list):
    return [word for word in word_list if word == word[::-1]]