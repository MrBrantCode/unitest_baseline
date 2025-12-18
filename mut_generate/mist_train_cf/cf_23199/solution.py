"""
QUESTION:
Develop a function `count_words` that takes a string as input and returns the number of unique words with at least 3 alphabetic characters. The function should consider words with hyphens or apostrophes as separate words, ignore leading/trailing spaces and punctuation marks, and handle cases with multiple spaces and mixed capitalization. The time complexity of the function should be O(n), where n is the length of the string.
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