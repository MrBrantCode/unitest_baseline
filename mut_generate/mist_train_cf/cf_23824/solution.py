"""
QUESTION:
Implement a function `is_palindrome(word)` that takes a string `word` as input and returns a boolean value indicating whether the word is the same forwards and backwards. The function should ignore case and non-alphanumeric characters are not part of the problem.
"""

def is_palindrome(word):
    """
    Checks if a given word is the same forwards and backwards, ignoring case and non-alphanumeric characters.

    Args:
        word (str): The input string to check.

    Returns:
        bool: True if the word is a palindrome, False otherwise.
    """
    cleaned_word = ''.join(e for e in word if e.isalnum()).lower()
    return cleaned_word == cleaned_word[::-1]