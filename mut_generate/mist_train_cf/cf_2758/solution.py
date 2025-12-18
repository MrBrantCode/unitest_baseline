"""
QUESTION:
Create a function named `count_unique_words` that takes in a string and returns the count of unique words in the string. The function should ignore any leading or trailing spaces in the string and handle punctuation marks and special characters by ignoring them while counting the words.
"""

import re

def count_unique_words(string):
    # Remove punctuation marks and special characters
    string = re.sub(r'[^\w\s]', '', string)

    # Remove leading and trailing spaces
    string = string.strip()

    # Split the string into a list of words
    words = string.split()

    # Return the count of unique words
    return len(set(words))