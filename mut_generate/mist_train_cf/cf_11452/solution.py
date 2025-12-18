"""
QUESTION:
Create a function called `is_palindrome` that takes a string as input. The function should return `True` if the string is a palindrome, ignoring non-alphanumeric characters and case, and `False` otherwise.
"""

def is_palindrome(word):
    # Convert the word to lowercase and remove non-alphanumeric characters
    cleaned_word = ''.join(c.lower() for c in word if c.isalnum())
    # Check if the cleaned word is equal to its reverse
    return cleaned_word == cleaned_word[::-1]