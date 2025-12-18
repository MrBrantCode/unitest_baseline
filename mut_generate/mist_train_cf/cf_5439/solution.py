"""
QUESTION:
Write a function `count_words` that takes a string as input, finds all the words that start with a caret (^) symbol, have at least 3 characters, and end with a lowercase vowel, ignoring leading or trailing spaces. The function should then count the total number of occurrences of each unique word found and the total number of unique words that contain a digit. Return the occurrences of each unique word and the total number of unique words with a digit. The words should be found using regular expression.
"""

import re
from typing import Dict

def count_words(string: str) -> Dict[str, int] and int:
    """
    This function takes a string as input, finds all the words that start with a caret (^) symbol, 
    have at least 3 characters, and end with a lowercase vowel, ignoring leading or trailing spaces.
    It counts the total number of occurrences of each unique word found and the total number of unique 
    words that contain a digit. It returns the occurrences of each unique word and the total number of 
    unique words with a digit.

    Args:
        string (str): Input string to be processed.

    Returns:
        Dict[str, int] and int: A dictionary of word occurrences and the total number of unique words with a digit.
    """

    # Remove leading and trailing spaces
    string = string.strip()

    # Find all words that match the regex pattern
    matches = re.findall(r'(?<!\S)\^[\w]{3,}[aeiou]\b(?!\S)', string)

    # Initialize counters
    total_occurrences = 0
    unique_words_with_digit = set()

    # Count occurrences and check for words with digits
    counts = {}
    for word in matches:
        counts[word] = counts.get(word, 0) + 1
        total_occurrences += 1
        if any(char.isdigit() for char in word):
            unique_words_with_digit.add(word)

    return counts, len(unique_words_with_digit)