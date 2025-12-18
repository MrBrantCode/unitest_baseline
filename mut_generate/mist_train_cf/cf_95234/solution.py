"""
QUESTION:
Write a function named `is_palindrome` that takes a string `word` as input, ignores spaces, punctuation, and capitalization, and returns `True` if the given word is a palindrome and `False` otherwise.
"""

def is_palindrome(word):
    # Convert the word to lowercase
    word = word.lower()

    # Remove non-alphanumeric characters
    word = ''.join(char for char in word if char.isalnum())

    # Check if the word is equal to its reverse
    return word == word[::-1]