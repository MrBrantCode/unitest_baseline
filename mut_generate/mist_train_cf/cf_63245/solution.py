"""
QUESTION:
Write a function named `count_unique_words` that takes a string as input and returns a dictionary containing the count of each unique word in the string. The function should be case-insensitive, consider punctuation as part of the word, and have a time complexity of O(N). The function should not use any built-in or library methods to count unique words. Implement the solution manually.
"""

import re

def count_unique_words(str):
    # Make the string case-insensitive
    str = str.lower()

    # Split words including punctuation as part of the word
    words = re.findall(r'\b\w[\w,!\?]*\b', str)

    # Count occurrence of each unique word
    unique_word_counts = {}
    for word in words:
        if word in unique_word_counts:
            unique_word_counts[word] += 1
        else:
            unique_word_counts[word] = 1

    return unique_word_counts