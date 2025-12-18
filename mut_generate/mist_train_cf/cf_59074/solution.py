"""
QUESTION:
Write a function `is_palindrome(text)` that determines whether a given text is a palindrome, ignoring case, non-alphanumeric characters, and supporting multilingual inputs. The function should return True if the text is a palindrome and False otherwise.
"""

def entrance(text):
    # Normalize the text by lowercasing it and removing non-alphanumeric characters
    text = "".join(char for char in text if char.isalnum()).lower()

    # Check if the text reads the same forwards and backward
    return text == text[::-1]