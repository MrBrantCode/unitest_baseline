"""
QUESTION:
Develop a function named `count_words` that takes a string as input and returns the count of unique words. Each word should be at least 3 characters long, consist only of alphabetic characters, and may include hyphens or apostrophes. The function should ignore leading or trailing spaces, handle multiple spaces between words, and handle mixed capitalization. The function should also have a time complexity of O(n), where n is the length of the string.
"""

import re

def count_words(string):
    # Remove leading and trailing spaces
    string = string.strip()

    # Remove punctuation marks except hyphens and apostrophes
    string = re.sub(r'[^\w\s\-\' ]', '', string)

    # Split the string into words
    words = string.split()

    # Normalize words to lowercase
    words = [word.lower() for word in words]

    # Remove words that are less than 3 characters long
    words = [word for word in words if len(word) >= 3]

    # Remove duplicates
    unique_words = list(set(words))

    # Return the count of unique words
    return len(unique_words)