"""
QUESTION:
Write a function named `count_word_occurrences` that takes a string as input and returns a dictionary with the occurrences of each word in the string. The function should consider only words that are at least three characters long and are case-sensitive. The input string is guaranteed to not contain punctuation marks or special characters.
"""

import re

def count_word_occurrences(input_string):
    # Remove punctuation and special characters
    clean_string = re.sub(r'[^\w\s]', '', input_string)

    # Split the string into words
    words = clean_string.split()

    # Initialize a dictionary to store word occurrences
    word_counts = {}

    # Iterate through each word
    for word in words:
        # Ignore words that are less than three characters long
        if len(word) >= 3:
            # Increment the word count in the dictionary
            word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts