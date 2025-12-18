"""
QUESTION:
Write a function `is_palindrome` that takes a string as input and returns `True` if the string is a palindrome and `False` otherwise. The function should ignore any leading or trailing spaces, non-alphabetic characters, and case differences. The input string should not exceed 100 characters.
"""

def is_palindrome(word):
    # Removing leading and trailing spaces
    word = word.strip()
    
    # Removing non-alphabetic characters
    word = ''.join(filter(str.isalpha, word))
    
    # Converting the word to lowercase
    word = word.lower()
    
    # Checking if the word is a palindrome
    return word == word[::-1]