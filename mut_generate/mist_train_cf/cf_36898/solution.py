"""
QUESTION:
Create a function called `count_unique_words` that takes a string as its parameter and returns a dictionary containing the unique words as keys and their respective counts as values. The function should ignore any non-alphabetic characters and treat uppercase and lowercase letters as equivalent. The word counts should be returned in descending order based on their occurrences.
"""

import re

def count_unique_words(input_string):
    word_counts = {}
    words = re.findall(r'\b\w+\b', input_string.lower())
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))