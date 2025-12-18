"""
QUESTION:
Write a function named `is_palindrome` that takes a string as input and returns a boolean value indicating whether the string is a palindrome or not. The function should ignore special characters, whitespace, punctuation, and consider accented characters or characters from non-Latin scripts as their base characters without accents. The comparison should be case-insensitive.
"""

import unicodedata
import re

def is_palindrome(s):
    # Normalize the string to remove accents and convert characters to lowercase
    normalized = unicodedata.normalize('NFD', s.lower())

    # Remove special characters, punctuation, and whitespace
    cleaned = re.sub(r'[^a-z0-9]', '', normalized)

    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]