"""
QUESTION:
Create a function called `is_palindrome(word)` that takes a string `word` as input and returns `True` if the word is a palindrome and `False` otherwise. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization. The input string may contain non-alphanumeric characters and the function should handle them correctly. The input only contains valid alphanumeric characters.
"""

def entrance(word):
    # Convert the word to lowercase
    word = word.lower()

    # Remove non-alphanumeric characters
    word = ''.join(char for char in word if char.isalnum())

    # Check if the word is equal to its reverse
    return word == word[::-1]