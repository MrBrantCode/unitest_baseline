"""
QUESTION:
Write a function named `count_unique_words` that takes a string paragraph as input and returns the count of unique words, excluding words less than 3 characters long, containing special characters or numbers, and ignoring case sensitivity. The function should also ignore a predefined list of common English words.
"""

import re

def count_unique_words(paragraph):
    # Ignore case sensitivity and convert the paragraph to lowercase
    paragraph = paragraph.lower()

    # Remove special characters and numbers from the paragraph
    paragraph = re.sub(r'[^a-zA-Z\s]', '', paragraph)

    # List of common English words to be ignored
    common_words = ['the', 'and', 'or', 'like']

    # Split the paragraph into individual words
    words = paragraph.split()

    # Filter out words less than 3 characters long and common English words
    words = [word for word in words if len(word) >= 3 and word not in common_words]

    # Create a set of unique words
    unique_words = set(words)

    # Return the count of unique words
    return len(unique_words)