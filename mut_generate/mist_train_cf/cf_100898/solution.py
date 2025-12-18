"""
QUESTION:
Write a function `is_palindrome` that takes a string `word` or `sentence` as input and returns `True` if it's a palindrome and `False` otherwise. The function should work with non-English alphabets and ignore case, diacritical marks, spaces, and non-alphanumeric characters.
"""

import unicodedata
import re

def is_palindrome(word):
    # Normalize the word and remove any diacritical marks
    normalized = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8')
    
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'\W+', '', normalized).lower()
    
    # Check if the cleaned word is equal to its reversed version
    return cleaned == cleaned[::-1]